import argparse
from typing import Dict

import pandas as pd

import classification_performance
from classifiers.classifier import Classifier
from classifiers.linear_regression_classifier import LinearRegressionClassifier
from classifiers.neural_networks.MLP import MLP
from classifiers.radom_forest_classifier import RandomForestClassifier
from classifiers.svm import SVM

from data_transformation.load_data import load_arff
from classifiers.neural_networks.network import NNClassifier
from classifiers.neural_networks.lstm import LSTM

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("unnamed", nargs=1, type=str)
    parser.add_argument(
        "-m",
        action="store_true",
        help="Measure model performance",
    )
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        help="Classifier type: \n'rf' - random forest\n'mlp' - multilayer perceptron\n'lr' - logistic regression",
        default='lr'
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Classifier type: \n'rf' - random forest\n'mlp' - multilayer perceptron\n'lr' - logistic regression",
        default="hist-tar-ind"
    )
    parser.add_argument(
        "-s",
        '--shuffle',
        help="Shuffle",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--learn",
        action="store_true",
        help="Apply transfer learning",
    )

    args = parser.parse_args()
    classifiers: Dict[str, any] = {
        "rf": RandomForestClassifier,
        "mlp": MLP,
        "lstm": LSTM,
        "lr": LinearRegressionClassifier,
        "svm": SVM
    }
    classifier: Classifier = None

    train_features, test_features, train_labels, test_labels, source_features, source_labels = load_arff(f"data/{args.path}.arff")

    for i in range(5): 
        train_features, test_features, train_labels, test_labels, source_features, source_labels = load_arff(f"data/{args.path}.arff")
        classifier = classifiers[args.type]()
        if args.learn:
            classifier.fit(source_features, source_labels, dry=True, shuffle=args.shuffle)
        classifier.fit(train_features, train_labels, shuffle=args.shuffle)

    if args.m:
        y = (classifier.predict(test_features) > 0.5) * 1
        cm = classification_performance.confusion_matrix(y, test_labels)
        with open(f'results/{"s_" if args.shuffle else ""}{"t" if args.learn else "n"}_{args.type}_{args.path}.txt', 'w') as writer:
            writer.writelines('Confusion matrix:' + str(cm))
            writer.writelines('Accuracy:' + str(classification_performance.accuracy(cm)))
            writer.writelines('precision:' + str(classification_performance.precision(cm)))
            writer.writelines('recall:' + str(classification_performance.recall(cm)))
            writer.writelines('f_measure:' + str(classification_performance.f_measure(cm)))
            train_acc, train_loss, val_acc, val_loss = NNClassifier.overall_performance()
            df = pd.DataFrame(list(zip(train_acc, train_loss, val_acc, val_loss)),
               columns =['train_acc', 'train_loss', 'val_acc', 'val_loss'])
            df.to_csv(f'results/{"s_" if args.shuffle else ""}{"t" if args.learn else "n"}_{args.type}_{args.path}.csv')


if __name__ == "__main__":
    main()
