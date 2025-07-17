#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

    return model.coef_


def main():
    coefficients = mystery_data()
    for i, coeff in enumerate(coefficients):
        print(f"Coefficient of X{i} is {coeff}")


if __name__ == "__main__":
    main()
