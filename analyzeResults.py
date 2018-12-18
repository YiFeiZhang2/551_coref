import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import sys
import argparse


def loadFile(filename):
    with open(filename) as f:
        data = json.load(f)
        return data


def loadFiles(filenames):
    all_epochs = [loadFile(f) for f in filenames]
    return all_epochs


def plotData(title, all_epochs):
    x = list(range(len(all_epochs)))

    # training_f1 = np.array([e['training_coref_f1'] for e in all_epochs])
    # validation_f1 = np.array([e['validation_coref_f1'] for e in all_epochs])
    # plt.plot(x, training_f1, label='Training')
    # plt.plot(x, validation_f1, label='Validation')

    precision = [e['validation_coref_precision'] for e in all_epochs]
    recall = [e['validation_coref_recall'] for e in all_epochs]
    f1 = [e['validation_coref_f1'] for e in all_epochs]

    precision = [0 if i < 62 else e for i, e in enumerate(precision)]
    recall = [0 if i < 62 else e for i, e in enumerate(recall)]
    f1 = [0 if i < 62 else e for i, e in enumerate(f1)]

    ax = plt.subplot(111)

    ax.plot(x, precision, label='Precision')
    ax.plot(x, recall, label='Recall')
    ax.plot(x, f1, label='F1')
    plt.ylabel('Score')
    plt.xlabel('Epochs')
    ax.legend(loc='upper center', bbox_to_anchor=(
        0.5, -0.05), shadow=True, ncol=3)
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    filenames = sys.argv[1:]
    all_epochs = loadFiles(filenames)
    plotData('Validation without ELMo', all_epochs)
