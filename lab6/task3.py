import pandas as pd

df = pd.read_csv('attacks.csv', encoding="ISO-8859-1")
fatal = df["Fatal"] == 'Y'
countries_fatal = df[fatal]
locations = countries_fatal['Country'].value_counts()

print(locations.head(6))
