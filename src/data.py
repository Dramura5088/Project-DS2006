import pandas as pd
from sklearn.model_selection import train_test_split

class Data():
    def __init__(self, data:pd.DataFrame):
        self.df = data
        self.features = self.df.drop("class")
        self.classes = self.df("class")

        self.normalSplit()
    
    def normalSplit(self):
        features_train, features_test, classes_train, classes_test = self.train_test_split(
            self.features, self.classes, test_size=0.2, random_state=10)

