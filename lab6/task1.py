# Lab 6 task 1
import pandas as pd


df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
locations = df['Location'].value_counts()

# print(type(locations))      this is a series
print(locations.head(1))
