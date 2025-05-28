#!/usr/bin/env python3

import pandas as pd


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", header=0, quotechar='"')
    print(f"Shape: {df.shape[0]}, {df.shape[1]}")
    print("Columns:")
    print("\n".join(str(col) for col in df.columns))


if __name__ == "__main__":
    main()
