#!/usr/bin/env python3

import sys
from math import sqrt


def summary(filename):
    with open(filename) as f:
        nums = []
        for line in f:
            try:
                nums.append(float(line))
            except ValueError:
                continue

        nums_sum = sum(nums)
        average = nums_sum / len(nums)
        stddev = sqrt(sum(map(lambda x: (x - average) ** 2, nums)) / (len(nums) - 1))

    return (nums_sum, average, stddev)


def main():
    for f in sys.argv[1:]:
        n_sum, average, stddev = summary(f)
        print(f"File: {f} Sum: {n_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")


if __name__ == "__main__":
    main()
