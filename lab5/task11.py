# Lab 5 task 11
import numpy as np
import pandas as pd

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    # from 0 to 1/3 of all rows
    hour = data[0:int(len(data)/3), 4]
    seasons = data[0:int(len(data)/3), 1]
    reg = data[0:int(len(data)/3), 14]

    df = pd.DataFrame({"Hour": hour, "Seasons": seasons, "Registered_Users": reg})
    print(df)

except IOError:
    print("The file is missing!")
