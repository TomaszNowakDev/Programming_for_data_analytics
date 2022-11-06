# Lab 5 task 10
import numpy as np
import pandas as pd

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    seasons = data[:, 1]
    temperature = data[:, 9]

    index = []
    for i in range(int(len(data))):
        index.append("a" + str(i))

    df = pd.DataFrame({"Seasons": seasons, "Temperature": temperature}, index=index)

    df[df["Temperature"] > 0.5] *= 41
    print(df)


except IOError:
    print("The file is missing!")
