# Lab 5 task 5
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    result = data[:, 13] > data[:, 14]
    result = data[result]

    percentage = len(result) / len(data)
    print(f"Percentage of days where there is more causal users: {format(percentage, '.4f')}%")


except IOError:
    print("The file is missing!")
