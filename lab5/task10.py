# Lab 5 task 10
import numpy as np
import pandas as pd

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    hour = data[:, 4]
    seasons = data[:, 1]
    reg = data[:, 14]

    df = pd.DataFrame({"Hour": hour, "Seasons": seasons, "Registered_Users": reg})
    print(df)


except IOError:
    print("The file is missing!")
