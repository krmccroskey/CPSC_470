Kilian McCroskey - CPSC 470
Spring 2022
Dr. Anil Shende
---------------------------

I. Root Directory Contents + Brief Info

Files (in root directory):
470_Demo.ipynp     -> Jupyter Notebook file containing basic usage of the models.
470_Scratch.ipynb  -> Jupyter Notebook file containing the code used to train the models.
constants.py       -> Python file containing constants for use by above code.
functions.py       -> Python file containing functions for use by above code.
README.txt         -> This ReadMe file.

Directories (from root):
/midi:                 -> Directory containing the training/test MIDI directories.
  /midi/atonal:        -> Directory containing all atonal training MIDI files.
    /midi/atonal/test: -> Directory containing all atonal test MIDI files.
  /midi/tonal:         -> Directory containing all tonal training MIDI files.
    /midi/tonal/test:  -> Directory containing all tonal test MIDI files.  
+------------------------------------------------------------------------------------
| All 'loose' files in each of the above directories are MIDI files, categorized by 
| directory. The files in '/midi/*/test' are distinct from any files in '/midi/*'.
| All files in '/midi/*' are used for training only.
+------------------------------------------------------------------------------------
     
/models:               -> Directory containing models exported during training.
+------------------------------------------------------------------------------------
| There are two types of files here. 
|  *.pkl -> exported model files. Formatted by X.Y.pkl; X is its classification (tonal
|           or atonal), Y is its score (0-100% accuracy).
|
|  .*-attributes.txt -> a .txt file containing the initialization statements for the
|                       respective tonal and atonal models.
+------------------------------------------------------------------------------------

II. Setup

This project is designed to be used with Jupyter Notebook. This software can be installed
in a variety of ways, but the most popular method is using the GUI of anaconda3 browser.

Anaconda can be installed here: https://docs.anaconda.com/anaconda/install/
From there, Jupyter Notebook can be installed from the 'home' menu.

The packages I used are mostly available to import via Jupyter; however there are a few
exceptions. 

1. hmmlearn

This is the package I used for training HMM's - this package is well-documented.

This package can be installed by running the following command in a 'conda' prompt:

   conda install -c conda-forge hmmlearn

2. mido

This is the package I used to interface with the MIDI files. It was instrumental to this
project.

This package can also be installed by typing the following command in a conda prompt:

   conda install -c conda-forge mido

Other than that, all dependencies should be good to go.

III. Usage

Once Jupyter is installed (with all dependencies), go ahead and run it.

It will run in your default web browser (unusual, I know...).

In the GUI, you'll want to navigate to the root directory of the code.

For the 'scratch' code (/470_Scratch.ipynb) - this is mostly for documenting how I
arrived at the model I got. The code may run fine, but I am not making any promises on that.

There are comments and code snippets that detail my train of thought throughout the process.

For the 'demo' code (/470_demo.ipynb) this is for demonstrating the working HMM classifiers.
This is meant to be ran, and should run with no errors. The final statement should show
the score of .91 accuracy in classifying tonality in the test sets.

The other .py files are for constants and functions, and I have documented them with
pre and post conditions as clearly as I could.


If you have any questions, I can be reached at krmccroskey(at)mail.roanoke.edu

Thanks!



