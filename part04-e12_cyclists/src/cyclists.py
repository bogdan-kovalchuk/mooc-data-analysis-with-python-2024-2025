#!/usr/bin/env python3

import pandas as pd


def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    return df


def main():
    print(cyclists().head())


if __name__ == "__main__":
    main()
