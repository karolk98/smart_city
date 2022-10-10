from typing import *

import numpy as np
from sklearn.model_selection import train_test_split
import arff
from sklearn import preprocessing


def load_arff(path="data/hist-tar-ind.arff", test_size=0.2) -> Tuple[np.ndarray, np.ndarray]:
    dataset = arff.load(open(path, 'r'))
    data = np.array(dataset['data'])
    data = data.astype(np.float32)
    data = preprocessing.normalize(data, axis=0, norm='max')
    source = data[np.where(data[:,0] == 1)]
    data = data[np.where(data[:,0] == 0)]
    X = data[:, 1:14]
    Y = data[:, 14]
    tX = source[:, 1:14]
    tY = source[:, 14]
    features, labels = X, Y

    return tuple(train_test_split(features, labels, test_size=test_size)) + (tX, tY)
