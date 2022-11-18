# Lab 6 task 8
import pandas as pd
pd.options.mode.chained_assignment = None

df = pd.read_csv("titanic.csv")
df['Embarked'][df['Embarked'] == 'C'] = 'Cherbourg'
df['Embarked'][df['Embarked'] == 'Q'] = 'Cobh'
df['Embarked'][df['Embarked'] == 'S'] = 'Southampton'

print(df)
df.to_csv('titanic_new.csv')
