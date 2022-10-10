from typing import List
from numpy import ndarray
from sklearn.ensemble import RandomForestRegressor

from classifiers.classifier import Classifier


class RandomForestClassifier(Classifier):
    def __init__(self, n=10):
        super().__init__()
        self.n = n

    def predict(self, features: ndarray) -> float:
        return self.rf.predict(features)

    def fit(self, features: ndarray, labels: ndarray) -> None:
        self.rf = RandomForestRegressor(n_estimators=self.n, random_state=42)
        self.rf.fit(features, labels, )
