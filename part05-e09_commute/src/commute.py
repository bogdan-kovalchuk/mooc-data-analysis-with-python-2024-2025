#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

WEEKDAY_MAP = {"ma": 1, "ti": 2, "ke": 3, "to": 4, "pe": 5, "la": 6, "su": 7}
MONTH_MAP = {
    "tammi": 1,
    "helmi": 2,
    "maalis": 3,
    "huhti": 4,
    "touko": 5,
    "kesä": 6,
    "heinä": 7,
    "elo": 8,
    "syys": 9,
    "loka": 10,
    "marras": 11,
    "joulu": 12,
}


def preprocess_date_column(df):
    # Extract components using regex
    date_parts = df["Päivämäärä"].str.extract(
        r"(?P<Weekday>\w+)\s(?P<Day>\d{1,2})\s(?P<Month>\w+)\s(?P<Year>\d{4})\s(?P<Hour>\d{1,2}):"
    )

    # Map weekday and month names to numbers
    date_parts["Weekday"] = date_parts["Weekday"].map(WEEKDAY_MAP)
    date_parts["Month"] = date_parts["Month"].map(MONTH_MAP)

    # Convert to correct dtypes
    date_parts = date_parts.astype({"Weekday": "int8", "Day": "int8", "Month": "int8", "Year": "int16", "Hour": "int8"})

    # Concatenate new date parts with original data (drop original Päivämäärä)
    df = pd.concat([date_parts, df.drop(columns=["Päivämäärä"])], axis=1)

    # Create datetime index
    df["Datetime"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])
    df = df.drop(columns=["Year", "Month", "Day", "Hour"])
    df = df.set_index("Datetime")

    return df


def commute():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(axis=1, how="all")
    df = preprocess_date_column(df)
    df = df.loc["2017-08-01":"2017-08-31"]
    return df.groupby("Weekday").sum()


def main():
    df = commute()
    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
