import pandas as pd
from data import Data


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


def yesOrNo(statement: str) -> bool:
    i = input(statement + "(y/n):")
    if i.lower() == "y":
        return True
    else:
        return False


def main():
    fileNotFound: bool = False
    doILoadBaseFile: bool = yesOrNo("Do you want to load the standard Dataset?")

    # Load base file
    if doILoadBaseFile == True:
        try:
            df = pd.read_csv("Mine_Dataset.csv")
        except:
            fileNotFound = True
            print("Base file not found. Switching to user selection.")
    # Let the user load a file
    elif fileNotFound or doILoadBaseFile == False:
        while True:
            try:
                filename = input("Type Dataset filename to load:")
                df = pd.read_csv(filename)
                break
            except:
                print("File not found or data was innacurate.")

    data: Data = Data(df)
    

    # Ronni from here
    


if __name__ == "__main__":
    main()
