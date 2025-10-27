import pandas as pd
from data import Data, createManualData
import mainMenuHelpFunctions as mMHF
from classifiers import Classifier_kNN, Classifier_Decision_Tree, Classifier


def main():
    df: pd.DataFrame = None
    dfTesting: pd.DataFrame = None
    dfCustom: pd.DataFrame = None

    data: Data = None
    model: Classifier = None

    userChoice: int
    modelChoice: int
    
    mainStatement = "Project DS2006\n"
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

                    print("Data Loaded:")  # Tells the user, clause in 3.a
                    data.evaluate()
                    input("Press ENTER to continue...")
                except:
                    df = None
                    data = None
                    input(
                        "Not able to load data. An unexpected error has occured. Is .csv formatting correct?"
                    )

            case 2:
                # Train model
                if data is None:  # Continue if data isnt loaded yet
                    input("Data needs to be loaded first.")
                    continue

                # Load and train model

                modelChoice = int(
                    input(
                        "\nSelect a Model:\n(1) k-Nearest Neightbors\n(2) Decision Tree\nChoice:"
                    )
                )

                match modelChoice:
                    case 1:
                        model = Classifier_kNN(data, k=3)
                        print("User Selected: kNN model")
                        model.evaluate()
                        input("Press ENTER to continue...")
                    case 2:
                        model = Classifier_Decision_Tree(data)
                        print("User selected: Decision Tree model")
                        model.evaluate()
                        input("Press ENTER to continue...")
                    case _:
                        input("Wrong input.")
                        continue

                if mMHF.yesOrNo("Do you want to save the evaluation?"):
                    model.saveEvaluation(filename=mMHF.getFilename() + ".txt")

            case 3:
                dfCustom = None  # RESET

                if model is None:  # Continue if model isnt trained yet
                    input("Model needs to be trained first.")
                    continue

                if mMHF.yesOrNo("Do you want to load the custom data from a file?"):
                    # Load a file and drop the mine type column.
                    dfCustom = mMHF.loadFile().drop("Mine_Type", axis=1)
                else:
                    # Load a custom row manually
                    dfCustom = pd.DataFrame()  # Create empty dataframe

                    for rows in range(
                        0,
                        mMHF.clamp(
                            mMHF.getIntInput(
                                "How many rows do you want to add?(Min: 1, Max: 10):"
                            ),
                            1,
                            10,
                        ),
                    ):
                        voltage = mMHF.clamp(
                            mMHF.getFloatInput(
                                "What's the voltage value of FLC sensor due to magnetic distortion? (Min: 0V, Max: 10.6V)"
                            ),
                            0.0,
                            10.6,
                        )
                        high = mMHF.clamp(
                            mMHF.getFloatInput(
                                "What's the height of the sensor from the ground? (Min: 0cm, Max: 20cm)"
                            ),
                            0.0,
                            20.0,
                        )
                        soilType = mMHF.clamp(
                            mMHF.getIntInput(
                                "What's the soil type depending on the moisture condition? (1-6)"
                            ),
                            1,
                            6,
                        )

                        dfCustom = pd.concat(
                            [
                                dfCustom,
                                createManualData(
                                    Voltage=voltage, High=high, Soil_Type=soilType
                                ),
                            ]
                        )

                prediction = model.predict(new_data=dfCustom)
                print(f"DataFrame:\n{dfCustom}")
                print(f"Prediction:\n{prediction}")
                input("Press ENTER to continue...")

            case _:
                print("Input Error\n")


if __name__ == "__main__":
    main()
