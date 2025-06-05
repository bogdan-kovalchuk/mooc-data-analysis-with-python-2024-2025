#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    def swap_name(name: str) -> str:
        """Capitalize and swap names if in 'Last, First' format."""
        name = name.title()
        if "," in name:
            last, first = name.split(",", 1)
            return f"{first.strip()} {last.strip()}"
        return name

    # Load dataset
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    # Normalize names: 'Last, First' → 'First Last'
    df["President"] = df["President"].apply(swap_name)
    df["Vice-president"] = df["Vice-president"].apply(swap_name)

    # Map textual season values to numbers (e.g. 'one' → 1)
    season_map = {"one": 1, "two": 2}
    df["Seasons"] = df["Seasons"].apply(lambda s: season_map.get(s, s))

    # Convert 'Last' column to numeric, coercing invalid values to NaN
    df["Last"] = pd.to_numeric(df["Last"], errors="coerce")

    # Extract 4-digit year from 'Start' column
    df["Start"] = df["Start"].str.extract(r"(\d{4})")[0].astype(float).astype("Int64")

    return df.astype({"President": object, "Start": int, "Last": float, "Seasons": int, "Vice-president": object})


def main():
    print(cleaning_data())


if __name__ == "__main__":
    main()
