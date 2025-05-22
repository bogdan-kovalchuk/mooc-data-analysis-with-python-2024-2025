#!/usr/bin/env python3

import numpy as np

# import scipy.linalg


def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))


def main():
    a = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    print(vector_lengths(a))


if __name__ == "__main__":
    main()
