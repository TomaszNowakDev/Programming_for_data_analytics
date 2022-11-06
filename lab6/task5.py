# Lab 6 task 5
import pandas as pd

df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")

fatal = df["Fatal"] == 'Y'
all_fatal = df[fatal]
print((len(all_fatal) / len(df)) * 100)
