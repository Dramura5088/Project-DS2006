from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from data import Data
import pandas as pd
import numpy as np


class Classifier(ABC):
    def __init__(self, data: Data):
        super().__init__()
        self.data = data

    # en metod för Evaluate som printar accuracy och classification report
    def evaluate(self):
        print("Accuracy:", accuracy_score(self.data.classes_test, self.predictions))
        print(classification_report(self.data.classes_test, self.predictions))

    def saveEvaluation(self, filename):
        with open(filename, "w") as file:
            write_string = f"Accuracy: {accuracy_score(self.data.classes_test, self.predictions)}\n"
            write_string += classification_report(
                self.data.classes_test, self.predictions
            )
            file.write(write_string)

    @abstractmethod
    def predict(self):
        pass


class Classifier_kNN(Classifier):

    def __init__(self, data: Data, k: int = 1):
        super().__init__(data=data)

        self.k = k
        self.knn = KNeighborsClassifier(n_neighbors=k)
        self.knn.fit(self.data.features_train, self.data.classes_train)
        self.predictions = self.knn.predict(self.data.features_test)

    def predict(self, new_data) -> np.ndarray:
        prediction = self.knn.predict(new_data)
        return prediction


class Classifier_Decision_Tree(Classifier):
    def __init__(self, data: Data):
        super().__init__(data=data)
        self.dt = DecisionTreeClassifier()
        self.dt.fit(self.data.features_train, self.data.classes_train)

        self.predictions = self.dt.predict(self.data.features_test)

    def predict(self, new_data) -> np.ndarray:
        prediction = self.dt.predict(new_data)
        return prediction
