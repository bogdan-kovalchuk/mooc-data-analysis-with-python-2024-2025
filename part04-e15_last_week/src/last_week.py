#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df["LW"] = pd.to_numeric(df["LW"].replace({"New": np.nan, "Re": np.nan}))

    df.loc[(df["Peak Pos"] == df["Pos"]) & (df["Pos"] < df["LW"]), "Peak Pos"] = np.nan

    last = pd.DataFrame({"Pos": np.arange(1, 41)})

    last_week_df = last.merge(
        df, left_on="Pos", right_on="LW", how="left", suffixes=("", "_old")
    )

    last_week_df["LW"] = np.nan

    last_week_df["WoC"] = last_week_df["WoC"] - 1

    mask_out = last_week_df["WoC"] <= 0
    last_week_df.loc[mask_out, ["Title", "Artist", "Publisher", "Peak Pos", "WoC"]] = (
        np.nan
    )

    cols = ["Pos", "LW", "Title", "Artist", "Publisher", "Peak Pos", "WoC"]
    return last_week_df[cols]


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:\n", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
