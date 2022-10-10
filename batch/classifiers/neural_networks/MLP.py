import torch
import torch.nn as nn
from typing import List
from classifiers.neural_networks.network import NNClassifier
import torch.nn.functional as F


def swish(x):
    return x * torch.relu(x)


features_count = 13


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(features_count, 30)
        self.fc2 = nn.Linear(30, 16)
        self.fc3 = nn.Linear(16, 1)
        self.dropout = nn.Dropout1d(0.25)

    def forward(self, x):
        x = swish(self.fc1(x))
        x = self.dropout(x)
        x = swish(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

# class Net(nn.Module):
#     def __init__(self, input_dim = 12, output_dim = 2):
#         super().__init__()

#         self.input_fc = nn.Linear(input_dim, 250)
#         self.hidden_fc = nn.Linear(250, 100)
#         self.output_fc = nn.Linear(100, 1)

#     def forward(self, x):

#         # x = [batch size, height, width]

#         batch_size = x.shape[0]

#         x = x.view(batch_size, -1)

#         # x = [batch size, height * width]

#         h_1 = F.relu(self.input_fc(x))

#         # h_1 = [batch size, 250]

#         h_2 = F.relu(self.hidden_fc(h_1))

#         # h_2 = [batch size, 100]

#         y_pred = torch.sigmoid(self.output_fc(h_2))

#         # y_pred = [batch size, output dim]

#         return y_pred

class MLP(NNClassifier):
    def __init__(self):
        super().__init__(Net())
