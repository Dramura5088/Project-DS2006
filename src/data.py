import pandas as pd
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self, data: pd.DataFrame):
        self.df = data
        self.features = self.df.drop("Mine_Type")
        self.classes = self.df("Mine_Type")

        self.normalSplit()

    def normalSplit(self):
        (
            self.features_train,
            self.features_test,
            self.classes_train,
            self.classes_test,
        ) = self.train_test_split(
            self.features, self.classes, test_size=0.2, random_state=10
        )
