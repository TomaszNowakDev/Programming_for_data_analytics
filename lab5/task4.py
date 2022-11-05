# Lab 5 task 4
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    no_holiday = data[data[:, 5] == 0]
    holiday = data[data[:, 5] == 1]

    print("Number of entries non-holiday: ", len(no_holiday))
    print("Number of entries holiday: ", len(holiday))
    print("Mean non-holiday", np.mean(no_holiday[:, 15]))
    print("Mean holiday", np.mean(holiday[:, 15]))

except IOError:
    print("The file is missing!")
