import pandas as pd

def getIntInput(statement:str) -> int:
    i:int
    while True:
        try:
            i = int(input(statement))
            break
        except:
            print("Invalid input.")


    return i

def yesOrNo(statement: str) -> bool:
    i = input(statement + "(y/n):")
    if i.lower().strip() == "y":
        return True
    else:
        return False

def loadBaseFile() -> pd.DataFrame:
    fileNotFound: bool = False
    doILoadBaseFile: bool = yesOrNo("Do you want to load the standard Dataset?")

    # Load base file
    if doILoadBaseFile == True:
        try:
            df = pd.read_csv("Mine_Dataset.csv")
            return df
        except:
            fileNotFound = True
            print("Base file not found. Switching to user selection.")
    # Let the user load a file
    if fileNotFound == True or doILoadBaseFile == False:
        return loadFile()

def loadFile() -> pd.DataFrame:
        while True: # While loop to get correct input.
            try:
                filename = input("Type Dataset filename to load:")
                df = pd.read_csv(filename)
                return df
            except:
                print("File not found or data was innacurate.")


