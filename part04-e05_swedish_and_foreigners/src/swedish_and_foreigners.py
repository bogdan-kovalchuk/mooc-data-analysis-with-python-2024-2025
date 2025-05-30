#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df_munic = df.loc["Akaa":"Äänekoski"]
    mask1 = df_munic["Share of Swedish-speakers of the population, %"] > 5.0
    mask2 = df_munic["Share of foreign citizens of the population, %"] > 5.0
    columns = [
        "Population",
        "Share of Swedish-speakers of the population, %",
        "Share of foreign citizens of the population, %",
    ]

    return df_munic.loc[mask1 & mask2, columns]


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
