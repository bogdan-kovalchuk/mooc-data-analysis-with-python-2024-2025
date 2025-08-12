#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(
    zip(
        "tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(),
        range(1, 13),
    )
)


def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)

    d = d.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )
    return d


def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    return pd.concat([d, df], axis=1)


def cycling_weather():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    bike = split_date_continues()
    bike = bike[bike.Year == 2017]
    bike = bike.groupby(["Year", "Month", "Day"]).sum()
    bike = bike.reset_index().drop(["Hour"], axis=1)
    result = wh.merge(
        bike, left_on=["Year", "m", "d"], right_on=["Year", "Month", "Day"]
    )

    return result.drop(["m", "d", "Time", "Time zone"], axis=1)


def cycling_weather_continues(station):
    df = cycling_weather()
    df = df.fillna(method="ffill")
    X = df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]]
    y = df[station]
    reg = LinearRegression()
    reg.fit(X, y)
    score = reg.score(X, y)
    return reg.coef_, score


def main():
    station = "Baana"
    coef, score = cycling_weather_continues(station)
    print("Measuring station:", station)
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
