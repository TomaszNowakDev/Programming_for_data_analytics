# Lab 6 task 4
import pandas as pd


df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
boolSurfAttacks = df["Activity"] == "Surfing"
boolScubaAttacks = df["Activity"] == "Scuba diving"

print("Number of attacks when surfing ", len(df[boolSurfAttacks]))
print("Number of attacks when Scuba Diving ", len(df[boolScubaAttacks]))
