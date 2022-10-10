import abc
from typing import List
from pandas import DataFrame
from numpy import ndarray


class Classifier(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def predict(self, features: List[float]) -> float:
        pass

    @abc.abstractmethod
    def fit(self, features: ndarray, labels: ndarray) -> None:
        pass
