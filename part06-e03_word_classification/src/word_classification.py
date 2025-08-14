#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)


# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode("utf-8"))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath("/kotus-sanalista/st/s")
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return list(lines)


def get_features(features: np.array):
    word_counters = [Counter(word) for word in features]
    return np.array([[counts.get(ch, 0) for ch in alphabet] for counts in word_counters])


def contains_valid_chars(string: str):
    return all(char in alphabet_set for char in string)


def get_features_and_labels():
    fin = [w.lower() for w in load_finnish() if contains_valid_chars(w.lower())]
    eng = [w.lower() for w in load_english() if contains_valid_chars(w[0]) and contains_valid_chars(w.lower())]
    X = get_features(fin + eng)
    y = np.array([0] * len(fin) + [1] * len(eng))
    return X, y


def word_classification():
    model = MultinomialNB()
    X, y = get_features_and_labels()
    kf = KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=kf, scoring="accuracy")
    return list(scores)


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
