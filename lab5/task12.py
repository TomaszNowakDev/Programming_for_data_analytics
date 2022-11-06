# Lab 5 task 12
import numpy as np
import pandas as pd

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    hour = data[:, 4]
    seasons = data[:, 1]
    reg = data[:, 14]

    index = []
    for i in range(int(len(data))):
        index.append("a" + str(i))

    df = pd.DataFrame({"Hour": hour, "Seasons": seasons, "Registered_Users": reg}, index=index)
    print(df)


except IOError:
    print("The file is missing!")
