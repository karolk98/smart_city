import numpy as np

def confusion_matrix(predicted, expected):
    true_positive = np.sum(np.logical_and(predicted == 1, expected == 1))
    false_positive = np.sum(np.logical_and(predicted == 1, expected == 0))
    true_negative = np.sum(np.logical_and(predicted == 0, expected == 0))
    false_negative = np.sum(np.logical_and(predicted == 0, expected == 1))
    return {
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "true_negative": true_negative
    }

def accuracy(conf_mat):
    full = conf_mat["true_positive"] + conf_mat["true_negative"] + \
           conf_mat["false_positive"] + conf_mat["false_negative"]
    return (conf_mat["true_positive"] + conf_mat["true_negative"]) / full


def precision(conf_mat):
    return conf_mat["true_positive"] / (conf_mat["true_positive"] + conf_mat["false_positive"])


def recall(conf_mat):
    return conf_mat["true_positive"] / (conf_mat["true_positive"] + conf_mat["false_negative"])


def f_measure(conf_mat):
    r = recall(conf_mat)
    p = precision(conf_mat)
    return 2 * (r * p) / (r + p)
