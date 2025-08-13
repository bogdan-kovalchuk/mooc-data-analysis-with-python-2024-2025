#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics


def plant_classification():
    iris_df = load_iris(as_frame=False)
    X_train, X_test, y_train, y_test = train_test_split(iris_df.data, iris_df.target, test_size=0.2, random_state=0)
    model = naive_bayes.GaussianNB()
    y_fitted = model.fit(X_train, y_train)
    labels_fitted = model.predict(X_test)
    return metrics.accuracy_score(labels_fitted, y_test)


def main():
    print(f"Accuracy is {plant_classification()}")


if __name__ == "__main__":
    main()
