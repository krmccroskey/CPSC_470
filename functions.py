#This .py file contains all the useful functions for creating/training/evaluating my HMM's.

#Imports
import constants

import numpy as np
from mido import MidiFile
from hmmlearn import hmm
import re
import os


#PRE: midi file is well formed, and is indeed a MidiFile object, and 're' module is imported
#POST: A 1D array containing the sequence of notes is returned
def extractNotes(midi):
    midi_text = str(midi)
    note_pattern = re.compile('note=(\d{1,3}),')
    
    #return removes unnecessary doubling of notes, caused by 'note_on' and 'note_off' messages
    note_list = note_pattern.findall(midi_text)[1::2]

    note_list_int = [int(i) for i in note_list]
    
    return np.reshape(note_list_int, [-1,1])


#PRE: Directory is well-defined and contains at least 1 Midifile.
#POST: Markov Chain is created and returned (raw chain data array, with length array).
#          Best used for getting the data and length in one object.
def createMarkovChain(directory):
    tracks = []
    track_lengths = []
    
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            extracted = extractNotes(MidiFile(file))
            tracks.extend(extracted)
            track_lengths.append(len(extracted))
            
    return [tracks, track_lengths]


#PRE: Models, arrays, and midifiles are well-defined.
#     Constants (paths to midi files) are correctly defined.
#POST: The tonality on the specified test midi directory are evaluated,
#      and returned as scored tonal, scored atonal, and total
#      with average scores of each model.
def evalTestDirectory(tonal_model, atonal_model, directory):
    scored_tonal = 0
    scored_atonal = 0
    tonal_scores = []
    atonal_scores = []
    
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            X = extractNotes(MidiFile(file))
            
            tonal_score = tonal_model.score(X)
            atonal_score = atonal_model.score(X)
            tonal_scores.append(tonal_score)
            atonal_scores.append(atonal_score)

            if(tonal_model.score(X) > atonal_model.score(X)):
                scored_tonal+=1
            else:
                scored_atonal+=1
        
    return ([scored_tonal, scored_atonal, np.average(tonal_scores), np.average(atonal_scores),])


#PRE: Models, arrays, and midifiles are well-defined.
#     Constants (paths to midi files) are correctly defined.
#POST: Percentages of correct predictions between the two models will be displayed.
#      This is accomplished by evaluating each midi file in a directory.
#      Results will be output in readable form, if verbose = true.

def score(tonal_model, atonal_model, verbose):
    
    print("Scoring...")
    
    #These are arrays - [#tonal, #atonal, avgTonalScore, avgAtonalScore, total]
    tonal_test = evalTestDirectory(tonal_model, atonal_model, constants.TONAL_TEST_DIR)
    atonal_test = evalTestDirectory(tonal_model, atonal_model, constants.ATONAL_TEST_DIR)
    
    correct = tonal_test[0] + atonal_test[1]
    incorrect = tonal_test[1] + atonal_test[0]
    total = correct + incorrect
    score = correct / total
    
    if (verbose == True):
        print("\nTonality:")
        print("Correct: " , correct)
        print("Inorrect: " , incorrect)
        print("Score:" , score)

    return score

    
    