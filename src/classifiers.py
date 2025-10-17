from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from data import Data


class Classifier_kNN:

    def __init__(self, data: Data):
        self.data = data

        self.knn = KNeighborsClassifier(n_neighbors=1)

        self.knn.fit(self.data.features_train, self.data.classes_train)

        self.predictions = self.knn.predict(self.data.features_test)

    # en metod för Evaluate som printar accuracy och classification report
    def evaluate(self):
        accuracy = accuracy_score(self, )
        report = classification_report(self, )
