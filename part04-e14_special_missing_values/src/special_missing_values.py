#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.replace(["New", "Re"], None, inplace=True)
    df["LW"] = pd.to_numeric(df["LW"])
    return df[df["Pos"] > df["LW"]]


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
