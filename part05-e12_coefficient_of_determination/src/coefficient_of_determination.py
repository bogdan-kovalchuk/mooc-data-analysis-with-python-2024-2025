#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y

    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, y)
    r2_score = model.score(X, y)

    r2_scores = []
    for x in X:
        model.fit(X[[x]], y)
        r2_scores.append(model.score(X[[x]], y))

    return [r2_score] + r2_scores


def main():
    r2_scores = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {r2_score[0]}")
    for i, coeff in enumerate(r2_scores[1:]):
        print(f"R2-score with feature(s) X{i}: {coeff}")


if __name__ == "__main__":
    main()
