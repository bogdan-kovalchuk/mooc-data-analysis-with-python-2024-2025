#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    dot_prod = np.sum(X * Y, axis=1)
    norm_X = np.sqrt(np.sum(X**2, axis=1))
    norm_Y = np.sqrt(np.sum(Y**2, axis=1))
    cos_theta = np.clip(dot_prod / (norm_X * norm_Y), -1, 1)
    angles_rad = np.arccos(cos_theta)
    return np.degrees(angles_rad)


def main():
    X = np.array([[1, 2, 4], [5, 6, 2]])
    Y = np.array([[3, 4, 1], [4, 5, 2]])
    print(vector_angles(X, Y))


if __name__ == "__main__":
    main()
