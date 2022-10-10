import torch
import torch.nn as nn
from typing import List
from classifiers.neural_networks.network import NNClassifier


def swish(x):
    return x * torch.sigmoid(x)


features_count = 13


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.lstm = nn.LSTM(features_count, 30)
        self.fc2 = nn.Linear(30, 16)
        self.fc3 = nn.Linear(16, 1)
        self.dropout = nn.Dropout1d(0.25)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = swish(x)
        x = swish(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

class LSTM(NNClassifier):
    def __init__(self):
        super().__init__(Net())
