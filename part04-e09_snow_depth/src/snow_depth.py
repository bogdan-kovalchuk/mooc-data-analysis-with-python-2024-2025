#!/usr/bin/env python3

import pandas as pd


def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df.loc[:, "Snow depth (cm)"].max()


def main():
    print(f"Max snow depth: {snow_depth():.2f}")


if __name__ == "__main__":
    main()
