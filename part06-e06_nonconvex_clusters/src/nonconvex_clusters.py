#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy

from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    X = df[["X1", "X2"]].to_numpy()
    y = df["y"].to_numpy()

    results = []
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        model.fit(X)

        labels_ = model.labels_
        n_clusters = np.unique(labels_[labels_ != -1]).size
        n_outliers = int(np.sum(labels_ == -1))

        score = np.nan
        if n_clusters == len(np.unique(y)):
            mask = labels_ != -1
            filtered_labels = labels_[mask]
            filtered_y = y[mask]
            permutation = find_permutation(n_clusters, filtered_y, filtered_labels)
            score = accuracy_score(filtered_labels, [permutation[label] for label in filtered_labels])

        results.append((eps, score, n_clusters, n_outliers))

    return pd.DataFrame(results, columns=["eps", "Score", "Clusters", "Outliers"]).astype(float)


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
