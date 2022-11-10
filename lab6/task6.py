# Lab 6 task 6
import pandas as pd

df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")

countries = pd.unique(df["Country"])
for c in countries:
    country = df['Country'] == c
    fatal = df["Fatal"] == 'Y'
    Non_Fatal = df["Fatal"] == 'N'

    country_fatal = df[country & fatal]
    country_non_Fatal = df[country & Non_Fatal]
    if len(country_fatal) > 0:
        print('The percentage of fatal attacks: ', c,
              len(country_fatal) * 100 / (len(country_fatal) + len(country_non_Fatal)))
