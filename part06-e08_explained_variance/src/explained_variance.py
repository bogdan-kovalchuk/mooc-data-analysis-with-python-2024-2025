#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


def explained_variance():
    filename = "src/data.tsv"
    df = pd.read_csv(filename, sep="\t")

    pca = PCA()
    pca.fit(df)

    variances = df.var(axis=0).values
    explained_variances = pca.explained_variance_
    return variances, explained_variances


def main():
    v, ev = explained_variance()
    print("The variances are:", " ".join(f"{x:.3f}" for x in v))
    print("The explained variances after PCA are:", " ".join(f"{x:.3f}" for x in ev))

    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
