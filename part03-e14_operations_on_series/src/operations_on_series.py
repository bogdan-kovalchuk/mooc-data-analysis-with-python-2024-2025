#!/usr/bin/env python3

import pandas as pd
import numpy as np


def create_series(L1, L2):
    s1 = pd.Series(L1, index=["a", "b", "c"])
    s2 = pd.Series(L2, index=["a", "b", "c"])
    return s1, s2


def modify_series(s1, s2):
    s1["d"] = s2["b"]
    s2.drop("b", inplace=True)
    return s1, s2


def main():
    L1 = np.array([1, 3, 5])
    L2 = np.array([2, 4, 8])
    s1, s2 = create_series(L1, L2)
    s1, s2 = modify_series(s1, s2)
    s = s1 + s2
    print(s)


if __name__ == "__main__":
    main()
