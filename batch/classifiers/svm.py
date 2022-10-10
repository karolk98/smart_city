from typing import List
from numpy import ndarray
from sklearn import svm

from classifiers.classifier import Classifier


class SVM(Classifier):
    def __init__(self):
        super().__init__()

    def predict(self, features: ndarray) -> float:
        return self.clf.predict(features)

    def fit(self, features: ndarray, labels: ndarray) -> None:
        self.clf = svm.SVC(kernel="rbf")
        self.clf.fit(features, labels )
