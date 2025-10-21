import pandas as pd


def clamp(n, min_value, max_value):
    """
    Clamps n between min_value and max_value using max and min functions together.

    Return:
        float or int:
            Returns clamped float or integer.
    """
    return max(min_value, min(n, max_value))


def getIntInput(statement: str) -> int:
    """
    Gets an int input from the user.

    Return:
        int:
            User input.
    """
    i: int
    while True:
        try:
            i = int(input(statement).strip())
            return i
        except:
            print("Invalid input.")


def getFloatInput(statement: str) -> float:
    """
    Gets an float input from the user.

    Return:
        float:
            User input.
    """
    f: float
    while True:
        try:
            f = int(input(statement).strip())
            return f
        except:
            print("Invalid input.")


def yesOrNo(statement: str) -> bool:
    """
    Simulates a yes or no question and returns a bool.

    Return:
        bool:
            Returns true if user input was 'y'. Otherwise it returns false.
    """
    i = input(statement + "(y/n):")
    if i.lower().strip() == "y":
        return True
    else:
        return False


def loadBaseFile() -> pd.DataFrame:
    """
    Prompts user to load base file. If the base file cannot be loaded it will always pass onto loadFile().
    Base file name is: Mine_Dataset.csv

    Returns:
        pd.DataFrame:
            Returns a dataFrame read from a .csv file.
    """
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
    """
    Prompts the user to load a .csv file after deciding a filename using the getFilename function.

    Returns:
        pd.DataFrame:
            Returns a dataFrame read from a .csv file.
    """
    while True:
        try:
            df = pd.read_csv(getFilename() + ".csv")
            return df
        except:
            print("Couldn't load file.")


def getFilename() -> str:
    """
    Prompts the user to pick a filename, either to load or save as.

    Returns:
        str:
            The choosen name stripped.
    """
    while True:
        try:
            filename = input(
                "Enter your desired filename(File ending not necessary):"
            ).strip()
            return filename
        except:
            print("Invalid filename")
            print(
                "Remember that the file endings are not necessary.\n EX: If you want to select example.txt then simply put 'example' as your desired file."
            )
