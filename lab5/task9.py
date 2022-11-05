# Lab 5 task 9
import numpy as np
import pandas as pd

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    index = np.array(np.arange(len(data)), str)

    d = pd.Series(data[:, 13], index=index)


except IOError:
    print("The file is missing!")
