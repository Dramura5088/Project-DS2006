import pandas as pd
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self, data: pd.DataFrame):
        self.df = data
        self.features = self.df.drop('Mine_Type', axis=1)
        self.classes = self.df['Mine_Type']

        
    def manualSplit(self, trainingData:pd.DataFrame):
        pass

    def normalSplit(self, stratify = False ,random_state = 10):
        (
            self.features_train,
            self.features_test,
            self.classes_train,
            self.classes_test,
        ) = self.train_test_split(
            self.features, self.classes, test_size=0.4, random_state=random_state, shuffle=True, stratify=stratify 
        )
    
    def evaluate(self):
        print("Head:\n" + self.df.head(10)) # Loads first 10 lines (requirement in 3.a)
        print("Describe:\n" + self.df.describe())
        print("Shape:\n" + self.df.shape)
