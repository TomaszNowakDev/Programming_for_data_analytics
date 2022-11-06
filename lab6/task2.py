# Lab 6 task 2
import pandas as pd


df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")

locations = df['Country'].value_counts()
print(locations.head(6))
