#!/usr/bin/env python3

import matplotlib.pyplot as plt


def main():
    plt.plot([2, 4, 6, 7], [4, 3, 5, 1])
    plt.plot([1, 2, 3, 4], [4, 2, 3, 1])
    plt.title("Exercise 3.9 (multiple graphs)")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()


if __name__ == "__main__":
    main()
