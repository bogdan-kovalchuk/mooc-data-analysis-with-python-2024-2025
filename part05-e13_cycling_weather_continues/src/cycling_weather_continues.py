#!/usr/bin/env python3
import pandas as pd
from sklearn import linear_model


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

    df = df.drop("Päivämäärä", axis=1)
    return pd.concat([date_parts, df], axis=1)


def cycling_weather():
    df1 = pd.read_csv("src/kumpula-weather-2017.csv", sep=",").dropna(how="all").dropna(axis=1, how="all")
    df2 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";").dropna(how="all").dropna(axis=1, how="all")
    df2 = split_date(df2)
    marged = pd.merge(df1, df2, left_on=["Year", "m", "d"], right_on=["Year", "Month", "Day"])
    return marged.drop(["m", "d", "Time", "Time zone"], axis=1).ffill()


def cycling_weather_continues(station=None):
    df = cycling_weather()
    X = df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]]
    y = df[[station]]
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, y)
    return (model.coef_, model.score(X, y))


def main():
    station = input("Measuring station: ")
    coefficients, score = cycling_weather_continues(station)
    c1, c2, c3 = coefficients[0]
    print(f"Regression coefficient for variable 'precipitation': {c1:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {c2:.1f}")
    print(f"Regression coefficient for variable 'temperature': {c3:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
