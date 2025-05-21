#!/usr/bin/env python3

import numpy as np


def diamond(n):
    eye = np.eye(n, dtype=int)
    flipped = np.flipud(eye[:, :-1])
    top = np.concatenate((flipped, eye), axis=1)
    bottom = np.flipud(top)[1:, :]
    full = np.concatenate((top, bottom), axis=0)
    return full


def main():
    print(diamond(4))


if __name__ == "__main__":
    main()
