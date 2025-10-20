import pandas as pd
from data import Data
import mainMenuHelpFunctions as mMHF
from classifiers import Classifier_kNN, Classifier_Decision_Tree, Classifier


"""
Requirement:
1. Choose data correctly. (DONE)
    Our data has 4 features and is for classification: https://archive.ics.uci.edu/dataset/763/land+mines-1

2. Make sure no other team is using it. (DONE)
    I checked so no other team was using it at the time. Then I posted it on the BB page to claim it.

3. Develop the Application (NOT DONE)
    a. Load the Dataset
        data.py manages loading and checking the files.

    b. Train a classification model with the current version of the dataset.
        classifiers.py manages classifying and checking the files.

    c. Evaluate and save the performance of the classification model.


    d. Simulate a real environment.


"""



def main():
    df:pd.DataFrame  = None
    data:Data        = None
    model:Classifier = None

    userChoice:int 
    
    mainStatement  = "Project DS2006\n"
    mainStatement += "By Philip H & Ronni E\n"
    mainStatement += "Choose option:\n"
    mainStatement += "(0) Exit\n"
    mainStatement += "(1) Load Data\n"
    mainStatement += "(2) Load Model\n"

    # Main Menu
    while True:
        # Gets user input
        userChoice = mMHF.getIntInput(statement=mainStatement)

        match userChoice:
            case 0:
                quit()
            case 1:
                # Load Data
                try:
                    df = mMHF.loadFile()
                    data = Data(df)

                    print("Data Loaded:") # Tells the user, clause in 3.a
                    data.evaluate()
                except:
                    print("Not able to load data. An unexpected error has occured. Is .csv formatting correct?")
                
            case 2: 
                # Train model
                if data is None: # Pass if data isnt loaded yet
                    input("Data needs to be loaded first.")
                    continue
                
                # Load and train model
                
                
            case _:
                print("Input Error\n")

if __name__ == "__main__":
    main()