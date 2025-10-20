import pandas as pd
from data import Data, createManualData
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
    dfTesting:pd.DataFrame = None
    dfCustom:pd.DataFrame = None

    data:Data        = None
    model:Classifier = None

    userChoice:int 
    modelChoice: int
    datasetChoice: int
    
    mainStatement  = "Project DS2006\n"
    mainStatement += "By Philip H & Ronni E\n"
    mainStatement += "Choose option:\n"
    mainStatement += "(0) Exit\n"
    mainStatement += "(1) Load Data\n"
    mainStatement += "(2) Load Model\n"
    mainStatement += "(3) Input Custom Example\n"
    mainStatement += "Choice:"

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
                    df = mMHF.loadBaseFile()
                  
                    if mMHF.yesOrNo("Do you want to load a file for testing?"):
                        dfTesting = mMHF.loadFile()

                    data = Data(df, dfTesting)


                    print("Data Loaded:") # Tells the user, clause in 3.a
                    data.evaluate()
                except:
                    df   = None
                    data = None
                    print("Not able to load data. An unexpected error has occured. Is .csv formatting correct?")
                
            case 2: 
                # Train model
                if data is None: # Continue if data isnt loaded yet
                    input("Data needs to be loaded first.")
                    continue
                
                # Load and train model

                modelChoice = int(input("\nSelect a Model:\n \nkNN Model(1)\n \nDecision Tree(2)\n"))
                
                match modelChoice:
                    case 1:
                        model = Classifier_kNN(data, k=3)
                        print("User Selected: kNN - model ")
                        model.evaluate()
                    case 2:
                        model = Classifier_Decision_Tree(data)
                        print("User selected: Decision Tree model")
                        model.evaluate()
                    case _:
                        print("Wrong input.")
                        continue
    
                if mMHF.yesOrNo("Do you want to save the evaluation?"):
                    model.saveEvaluation(filename=mMHF.getFilename()+".txt")

            case 3:
                dfCustom = None # RESET

                if model is None: # Continue if model isnt trained yet
                    input("Model needs to be trained first.")
                    continue

                if mMHF.yesOrNo("Do you want to load the custom data from a file?"):
                    # Load a file
                    dfCustom = mMHF.loadFile()
                else:
                    # Load a custom row manually

                    dfCustom = pd.DataFrame() # Create empty dataframe
                    for rows in range(0,mMHF.clamp(mMHF.getIntInput("How many rows do you want to add?(Max 10):"), 0, 10)):
                        voltage  = mMHF.clamp(mMHF.getFloatInput("What's the voltage value of FLC sensor due to magnetic distortion? (Min: 0V, Max: 10.6V)"),0.0,10.6)
                        high     = mMHF.clamp(mMHF.getFloatInput("What's the height of the sensor from the ground? (Min: 0cm, Max: 20cm)"),0.0,20.0)
                        soilType = mMHF.clamp(mMHF.getIntInput("What's the soil type depending on the moisture condition? (1-6)"),1,6)

                        dfCustom = pd.concat([dfCustom ,createManualData(Voltage=voltage, High=high, Soil_Type=soilType)])
                
                prediction = model.predict(dfCustom)
                print("DataFrame:\n", dfCustom)
                print("Prediction:\n", prediction)
                        
                            
                    



            case _:
                print("Input Error\n")

if __name__ == "__main__":
    main()








