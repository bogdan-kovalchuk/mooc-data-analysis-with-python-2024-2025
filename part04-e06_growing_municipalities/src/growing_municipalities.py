#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):
    all_population = df.shape[0]
    grows = df[df["Population change from the previous year, %"] > 0].shape[0]
    return grows / all_population


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    print(f"Proportion of growing municipalities: {growing_municipalities(df):.1f}%")


if __name__ == "__main__":
    main()
