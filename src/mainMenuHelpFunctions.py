import pandas as pd


def clamp(n, min_value, max_value):
    return max(min_value, min(n, max_value))


def getIntInput(statement: str) -> int:
    i: int
    while True:
        try:
            i = int(input(statement))
            return i
        except:
            print("Invalid input.")


def getFloatInput(statement: str) -> float:
    f: float
    while True:
        try:
            f = int(input(statement))
            return f
        except:
            print("Invalid input.")


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
    while True:
        try:
            df = pd.read_csv(getFilename() + ".csv")
            return df
        except:
            print("Couldn't load file.")


def getFilename() -> str:
    while True:
        try:
            filename = input("Enter your desired filename: ").strip()
            return filename
        except:
            print("Invalid filename")
