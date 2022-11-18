# Lab 6 task 7
import pandas as pd

df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
print("Data available for countries", df['Country'].unique())
c_list = df['Country'].unique()


def country(c):
    country_bool = df['Country'] == c

    for yr in pd.unique(df['Year']):
        if 1924 < yr < 2016:
            yeah_bool = df['Year'] == yr
            country_year = df[country_bool & yeah_bool]
            print(f"{c} year:{int(yr)}, number of shark attacks:{len(country_year)}")


cont = True
while cont:
    while True:
        try:
            cou = input("Enter name of country from the list >>>")
            if cou in c_list:
                break
        except ValueError:
            print("Type in name of country from the list!")
    country(cou)

    while True:
        try:
            choice = input("Another country? [y/n]").lower()
            if choice == 'y' or choice == 'n':
                break
            else:
                print("Please enter \"y\" or \"n\"")
        except ValueError:
            print("Type 'y' or 'n'")
    if choice == 'n':
        cont = False
