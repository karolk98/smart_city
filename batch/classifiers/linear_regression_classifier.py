from typing import List
from numpy import ndarray
from sklearn import linear_model

from classifiers.classifier import Classifier


class LinearRegressionClassifier(Classifier):
    def __init__(self):
        super().__init__()

    def predict(self, features: ndarray) -> float:
        return self.clf.predict(features)

    def fit(self, features: ndarray, labels: ndarray) -> None:
        self.clf = linear_model.LinearRegression()
        self.clf.fit(features, labels )