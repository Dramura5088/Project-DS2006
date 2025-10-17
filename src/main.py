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
    df:pd.DataFrame
    data:Data
    model:Classifier

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
                df = mMHF.loadFile()
                data = Data(df)
                pass
            case 2:
                # Train model
                pass
            case _:
                print("Input Error\n")





    #df:pd.DataFrame = mainMenu.loadFile()
    #data = Data(data=df)
    




    # Ronni from here
    
    #model:Classifier = None
    while True:
        try: 
            userChoice = int(input("Choose between the two classification models: kNN(1) or Decision Tree(2)").strip())
            match userChoice:
                case 1:
                    model = Classifier_kNN(data)
                    break
                case 2:
                    model = Classifier_Decision_Tree(data)
                    break
                case _:
                    print("Invalid Input")   
        except:
             print("Invalid input")
    model.evaluate()
   
        
            
        
       
        
        
    


if __name__ == "__main__":
    main()
