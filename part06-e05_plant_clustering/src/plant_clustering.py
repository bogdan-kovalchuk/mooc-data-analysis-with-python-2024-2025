#!/usr/bin/env python3

import sklearn
import scipy

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def plant_clustering():
    X, y = load_iris(return_X_y=True)
    model = KMeans(n_clusters=3, n_init=10, random_state=0)
    model.fit(X)
    permutation = find_permutation(3, y, model.labels_)
    return sklearn.metrics.accuracy_score(y, [permutation[label] for label in model.labels_])


def main():
    print(plant_clustering())


if __name__ == "__main__":
    main()
