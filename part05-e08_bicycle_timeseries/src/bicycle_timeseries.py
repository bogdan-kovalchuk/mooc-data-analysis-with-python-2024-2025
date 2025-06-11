#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    date_parts = df["Päivämäärä"].str.extract(
        r"(?P<Weekday>\w+)\s(?P<Day>\d{1,2})\s(?P<Month>\w+)\s(?P<Year>\d{4})\s(?P<Hour>\d{1,2}):\d{2}"
    )

    weekday_map = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }

    month_map = {
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

    date_parts["Weekday"] = date_parts["Weekday"].map(weekday_map)
    date_parts["Month"] = date_parts["Month"].map(month_map)

    date_parts = date_parts.astype({"Day": int, "Month": int, "Year": int, "Hour": int})

    return pd.concat([date_parts, df], axis=1)


def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(axis=1, how="all")
    df = split_date(df)
    df["Päivämäärä"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])
    df = df.drop(["Weekday", "Day", "Month", "Year", "Hour"], axis=1)
    df = df.set_index("Päivämäärä")

    return df


def main():
    print(bicycle_timeseries())


if __name__ == "__main__":
    main()
