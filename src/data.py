import pandas as pd
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self, data: pd.DataFrame, preDeterminedTestingData: pd.DataFrame = None, doStratify:bool = False, random_state = 10):
        
        if preDeterminedTestingData is not None and self.dataLeakageCheck(data, preDeterminedTestingData):
            print("A Data leakage has been found. The predictions will now be unreliable. Load new data.")


        self.df = data 
        self.features = self.df.drop('Mine_Type', axis=1)
        self.classes = self.df['Mine_Type']
        
        
        if preDeterminedTestingData is None:
            # Train test split
            stratify = None # Set stratify
            if doStratify is True:
                stratify = self.classes
                
            self.normalSplit(stratify=stratify, random_state=random_state)
        else:
            self.manualSplit(trainingData=data, testingData=preDeterminedTestingData)


        
    def manualSplit(self, trainingData:pd.DataFrame, testingData:pd.DataFrame):
        # Hard coded setup.
        self.features_train = trainingData.drop('Mine_Type', axis=1)
        self.classes_train  = trainingData['Mine_Type']
    
        self.features_test  = testingData.drop('Mine_Type', axis=1)
        self.classes_test   = testingData['Mine_Type']

    def normalSplit(self, stratify, random_state = 10):
        (
            self.features_train,
            self.features_test,
            self.classes_train,
            self.classes_test,
        ) = train_test_split(
            self.features, self.classes, test_size=0.4, random_state=random_state, shuffle=True, stratify=stratify 
        )
    
    def evaluate(self):
        print(f"Head:\n{self.df.head(10)}" ) # Loads first 10 lines (requirement in 3.a)
        print(f"Describe:\n{self.df.info()}")
        print(f"Shape:\n{self.df.shape}")

    def dataLeakageCheck(self, trainingData:pd.DataFrame, testData:pd.DataFrame) -> bool:
        """
        Return:
            Bool:
                Returns true if a data leakage is found.
        """
        # Makes a new dataFrame with bools for overlaps.
        checkdf:pd.DataFrame = testData.isin(trainingData)

        # Makes a mask to get only the duplicates.
        mask = (checkdf["Voltage"] == True) & (checkdf["High"] == True) & (checkdf["Soil_Type"] == True)

        if checkdf[mask].empty == True: # If there is not data leak
            return False
        else:
            return True
        
def createManualData(Voltage:float, High:float, Soil_Type:float) -> pd.DataFrame:
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
    """
    # Mean
    Voltage = (Voltage - 0) / (10.6 - 0)
    High    = (High - 0) / (20 - 0)

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

    df = pd.DataFrame([Voltage, High, Soil_Type])
    return df