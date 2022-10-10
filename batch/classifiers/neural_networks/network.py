from pickle import NONE
from typing import List
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data

import torchvision.transforms as transforms
import torchvision.datasets as datasets

from sklearn import metrics
from sklearn import decomposition
from sklearn import manifold
from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
import numpy as np

import random

from classifiers.classifier import Classifier
BATCH_SIZE = 128
EPOCHS = 40
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class NNClassifier(Classifier):
    SEED = 1
    TOTAL = 0
    SIZE = -1
    TRAIN_ACC = []
    VAL_ACC = []
    TRAIN_LOSS = []
    VAL_LOSS = []

    def __init__(self, network):
        super().__init__()
        self.net = network
        random.seed(NNClassifier.SEED)
        np.random.seed(NNClassifier.SEED)
        torch.manual_seed(NNClassifier.SEED)
        torch.cuda.manual_seed(NNClassifier.SEED)
        torch.backends.cudnn.deterministic = True
        NNClassifier.SEED = NNClassifier.SEED + 1
        NNClassifier.TOTAL = NNClassifier.TOTAL + 1

    # def overall_performance():
    #     train_acc = np.array(NNClassifier.TRAIN_ACC).reshape((NNClassifier.TOTAL, EPOCHS)).mean(axis=0)
    #     val_acc = np.array(NNClassifier.VAL_ACC).reshape((NNClassifier.TOTAL, EPOCHS)).mean(axis=0)
    #     train_loss = np.array(NNClassifier.TRAIN_LOSS).reshape((NNClassifier.TOTAL, EPOCHS)).mean(axis=0)
    #     val_loss = np.array(NNClassifier.VAL_LOSS).reshape((NNClassifier.TOTAL, EPOCHS)).mean(axis=0)
    #     return train_acc, train_loss, val_acc, val_loss

    def overall_performance():
        train_acc = np.array(NNClassifier.TRAIN_ACC).reshape((NNClassifier.TOTAL, -1)).mean(axis=0)
        val_acc = np.array(NNClassifier.VAL_ACC).reshape((NNClassifier.TOTAL, -1)).mean(axis=0)
        train_loss = np.array(NNClassifier.TRAIN_LOSS).reshape((NNClassifier.TOTAL, -1)).mean(axis=0)
        val_loss = np.array(NNClassifier.VAL_LOSS).reshape((NNClassifier.TOTAL, -1)).mean(axis=0)
        return train_acc, train_loss, val_acc, val_loss

    def predict(self, features: np.ndarray) -> List[float]:
        self.net.eval()
        output = self.net(torch.Tensor(features)).detach().numpy()
        return output.reshape(len(output))

    # def fit(self, features: ndarray, labels: ndarray) -> None:
    #     self.net.train()
    #     optimizer = Adam(self.net.parameters(), lr=0.02)
    #     criterion = nn.MSELoss()

    #     train_features = torch.Tensor(features)
    #     train_labels = torch.Tensor(labels).resize(len(labels), 1)
    #     self.net.zero_grad()
    #     for epoch in range(EPOCHS):
    #         loss, predictions = train(self.net, train_features, train_labels, optimizer, criterion)
    #         if epoch % 40 == 0:
    #             predictions = np.reshape((predictions.data.numpy() > 0.5) * 1, len(predictions))
    #             accuracy = np.mean(predictions == labels)
    #             print(f"Epoch {epoch + 1} Accuracy : {accuracy}, Loss : {loss}")
    #     self.net.eval()

    def fit(self, features: np.ndarray, labels: np.ndarray, dry=False, shuffle=False) -> None:
        train_features, valid_features, train_labels, valid_labels = tuple(train_test_split(features, labels, test_size=int(features.shape[0]*0.1)))
        train_features = torch.Tensor(train_features)
        train_labels = torch.Tensor(train_labels).resize(len(train_labels), 1)
        train = torch.utils.data.TensorDataset(train_features, train_labels)
        train_loader = torch.utils.data.DataLoader(train, batch_size=BATCH_SIZE, shuffle=shuffle)
        valid_features = torch.Tensor(valid_features)
        valid_labels = torch.Tensor(valid_labels).resize(len(valid_labels), 1)
        valid = torch.utils.data.TensorDataset(valid_features, valid_labels)
        valid_loader = torch.utils.data.DataLoader(valid, batch_size=BATCH_SIZE, shuffle=shuffle)
        optimizer = optim.Adam(self.net.parameters(), lr=0.002)
        criterion = nn.BCELoss().to(device)

        for epoch in range(EPOCHS):

            train_loss, train_acc = self.train(train_loader, optimizer, criterion, device, valid_loader if not dry else None)
            valid_loss, valid_acc = self.evaluate(valid_loader, criterion, device)
            if not dry:
                NNClassifier.VAL_ACC.append(valid_acc)
                NNClassifier.TRAIN_ACC.append(train_acc)
                NNClassifier.VAL_LOSS.append(valid_loss)
                NNClassifier.TRAIN_LOSS.append(train_loss)

            print(f'Epoch: {epoch+1:02}')
            print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
            print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
    
    def evaluate(self, iterator, criterion, device):
        epoch_loss = 0
        epoch_acc = 0

        self.net.eval()

        with torch.no_grad():

            for (x, y) in iterator:

                x = x.to(device)
                y = y.to(device)

                y_pred = self.net(x)

                loss = criterion(y_pred, y)

                acc = calculate_accuracy(y_pred, y)
                epoch_loss += loss.item()
                epoch_acc += acc.item()

        return epoch_loss / len(iterator), epoch_acc / len(iterator)

    def train(self, iterator, optimizer, criterion, device, valid_iterator):
        epoch_loss = 0
        epoch_acc = 0

        for (x, y) in iterator:
            self.net.train()

            x = x.to(device)
            y = y.to(device)

            optimizer.zero_grad()

            y_pred = self.net(x)

            loss = criterion(y_pred, y)

            acc = calculate_accuracy(y_pred, y)

            loss.backward()

            optimizer.step()

            epoch_loss += loss.item()
            epoch_acc += acc.item()
            # if valid_iterator:
            #     valid_loss, valid_acc = self.evaluate(valid_iterator, criterion, device)
            #     train_loss, train_acc = (loss.item(), acc.item())
            #     NNClassifier.VAL_ACC.append(valid_acc)
            #     NNClassifier.TRAIN_ACC.append(train_acc)
            #     NNClassifier.VAL_LOSS.append(valid_loss)
            #     NNClassifier.TRAIN_LOSS.append(train_loss)

        return epoch_loss / len(iterator), epoch_acc / len(iterator)

def calculate_accuracy(y_pred, y):
    top_pred = torch.round(y_pred)
    correct = top_pred.eq(y.view_as(top_pred)).sum()
    acc = correct.float() / y.shape[0]
    return acc


# def train(model, x, y, optimizer, criterion):
#     optimizer.zero_grad()
#     output = model(x)
#     loss = criterion(output, y)
#     loss.backward()
#     optimizer.step()

#     return loss, output

def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs