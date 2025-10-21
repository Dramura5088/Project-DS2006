import pandas as pd
from sklearn.model_selection import train_test_split


class Data:
    def __init__(
        self,
        data: pd.DataFrame,
        preDeterminedTestingData: pd.DataFrame = None,
        doStratify: bool = True,
        random_state=10,
    ):
        """
        Passes base values to the data class.
        data:
            Base data, if preDeterminedTestingData is null then it will automatically be divided into testing and training data.
        preDeterminedTestingData:
            Will trigger a manual split if a dataFrame is provided. The Data variable will be training data and this will be testing data.
        doStratify:
            Only applies if preDeterminedTestingData is None. Will stratify the split after Mine Types.
        random_state:
            Dictates the random state.

        Return:
            No return. But sets class attributes: df, features, classes, features_train, classes_train, features_test, classes_test
        """

        # Checks for dataLeakage and informs the user if we are using preDeterminedTestingData.
        if preDeterminedTestingData is not None and self.dataLeakageCheck(
            data, preDeterminedTestingData
        ):
            input(
                "A Data leakage has been found. The predictions will now be unreliable. Load new data and model."
            )

        self.df = data
        self.features = self.df.drop("Mine_Type", axis=1)
        self.classes = self.df["Mine_Type"]

        if preDeterminedTestingData is None:

            # Set stratify
            stratify = None
            if doStratify is True:
                stratify = self.classes

            # Train test split
            self.normalSplit(stratify=stratify, random_state=random_state)
        else:
            self.manualSplit(trainingData=data, testingData=preDeterminedTestingData)

    def manualSplit(self, trainingData: pd.DataFrame, testingData: pd.DataFrame):
        """
        trainingData:
            Data to be trained.
        testingData:
            Data to be tested.

        Returns:
            No return. But sets class attributes: features_train, classes_train, features_test, classes_test
        """

        # Hard coded setup.
        self.features_train = trainingData.drop("Mine_Type", axis=1)
        self.classes_train = trainingData["Mine_Type"]

        self.features_test = testingData.drop("Mine_Type", axis=1)
        self.classes_test = testingData["Mine_Type"]

    def normalSplit(self, stratify, random_state=10):
        """
        Splits self.features, and self.classes using the train_test_split from scikit-learn train_test_split.

        stratify:
            stratify setting.

        random_state:
            random state.

        Return:
            No return. But sets class attributes: features_train, classes_train, features_test, classes_test
        """
        (
            self.features_train,
            self.features_test,
            self.classes_train,
            self.classes_test,
        ) = train_test_split(
            self.features,
            self.classes,
            test_size=0.4,
            random_state=random_state,
            shuffle=True,
            stratify=stratify,
        )

    def evaluate(self):
        """
        Prints statements for data evaluation.

        Return:
            No return.
        """

        print(f"Head:\n{self.df.head(10)}")  # Loads first 10 lines (requirement in 3.a)
        print(f"Describe:\n{self.df.describe()}")
        print(f"Shape:\n{self.df.shape}")

    def dataLeakageCheck(
        self, trainingData: pd.DataFrame, testData: pd.DataFrame
    ) -> bool:
        """
        Return:
            Bool:
                Returns true if a data leakage is found.
        """
        # Makes a new dataFrame with bools for overlaps.
        checkdf: pd.DataFrame = testData.isin(trainingData)

         # Makes a mask to get only rows with all True.
        mask = (
            (checkdf["Voltage"] == True)
            & (checkdf["High"] == True)
            & (checkdf["Soil_Type"] == True)
        )

        if checkdf[mask].empty == True:  # If there is no data leak
            return False
        else:
            return True


def createManualData(Voltage: float, High: float, Soil_Type: float) -> pd.DataFrame:
    """
    Values input are to be based on the original values according to the dataset.

        Voltage:
            Output voltage value of FLC sensor due to magnetic distortion
            Between 0V - 10.6V

        High:
            The height of the sensor from the ground
            Between 0cm - 20cm

        Soil Type:
            6 different soil types depending on the moisture condition.
            1(0.0) Dry and Sandy
            2(0.2) Dry and Humus
            3(0.4) Dry and Limy
            4(0.6) Humid and Sandy
            5(0.8) Humid and Humus
            6(1.0) Humid and Limy

        Return:
            pd.DataFrame:
                correctly formated data for testing. Data is normalized using min-max.
    """
    # Mean
    Voltage = (Voltage - 0) / (10.6 - 0)
    High = (High - 0) / (20 - 0)

    # Switch
    match Soil_Type:
        case 1:
            Soil_Type = 0.0
        case 2:
            Soil_Type = 0.2
        case 3:
            Soil_Type = 0.4
        case 4:
            Soil_Type = 0.6
        case 5:
            Soil_Type = 0.8
        case 6:
            Soil_Type = 1.0

    # df = pd.DataFrame(data=[[Voltage], [High], [Soil_Type]], columns=["Voltage","High","Soil_Type"])
    df = pd.DataFrame(
        data={"Voltage": [Voltage], "High": [High], "Soil_Type": Soil_Type}
    )
    return df
