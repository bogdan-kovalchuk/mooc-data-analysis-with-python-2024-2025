#!/usr/bin/env python3
import gzip
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=1.0):
    with gzip.open("src/spam.txt.gz", "rt", encoding="utf-8") as f:
        all_lines = f.readlines()
        count = int(len(all_lines) * fraction)
        spam = all_lines[:count]

    with gzip.open("src/ham.txt.gz", "rt", encoding="utf-8") as f:
        all_lines = f.readlines()
        count = int(len(all_lines) * fraction)
        ham = all_lines[:count]

    all_emails = ham + spam

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_emails)

    y = np.array([0] * len(ham) + [1] * len(spam))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state
    )

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    misclassified = sum(
        y_pred_i != y_true_i for y_pred_i, y_true_i in zip(y_pred, y_test)
    )

    return accuracy, len(y_test), misclassified


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
