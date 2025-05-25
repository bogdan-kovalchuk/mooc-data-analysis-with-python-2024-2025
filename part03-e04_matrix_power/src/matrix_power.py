#!/usr/bin/env python3

import numpy as np
from functools import reduce


from functools import reduce
import numpy as np


def matrix_power(a, n):
    if n < 0:
        a = np.linalg.inv(a)
    return reduce(
        np.matmul, (a for _ in range(abs(n))), np.eye(a.shape[0], dtype=a.dtype)
    )


def main():
    print(matrix_power(np.array([[1, 2], [3, 4]]), 3))


if __name__ == "__main__":
    main()
