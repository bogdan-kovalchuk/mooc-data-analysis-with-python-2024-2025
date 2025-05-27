#!/usr/bin/env python3
import pandas as pd


def read_series():
    result = pd.Series([])
    while True:
        user_input = input()
        if not user_input:
            break
        idx, val = user_input.split()
        result[idx] = val
    return result


def main():
    print(read_series())


if __name__ == "__main__":
    main()
