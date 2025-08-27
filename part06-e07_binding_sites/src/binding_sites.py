#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns

sns.set(color_codes=True)
import scipy
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def toint(x):
    return {"A": 0, "C": 1, "G": 2, "T": 3}[x]


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    X = df["X"].apply(list).apply(pd.Series).applymap(toint).to_numpy()
    y = df["y"].to_numpy()
    return X, y


def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(2, linkage="average", metric="euclidean")
    y_fitted = clustering.fit_predict(X)
    return accuracy_score(y, y_fitted)  # 0.9865


def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(2, linkage="average", metric="precomputed")
    dist_matrix = pairwise_distances(X, metric="hamming")
    y_fitted = 1 - clustering.fit_predict(dist_matrix)
    return accuracy_score(y, y_fitted)  # 0.9975


def main():
    print("Accuracy score with Euclidean metric is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming metric is", cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
