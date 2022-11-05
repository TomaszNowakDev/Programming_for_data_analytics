# Lab 5 task 8
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')
    for hour in range(0, 24, 6):
        lowHour = data[:, 4] >= hour
        highHour = data[:, 4] < hour + 6
        hours = data[lowHour & highHour]
        averageTotal = np.mean(hours[:, 15])
        averageCasual = np.mean(hours[:, 13])
        averageRegistered = np.mean(hours[:, 14])
        print(f"From {hour} to {hour + 6} average total users: {averageTotal}")
        print(f"From {hour} to {hour + 6} average casual users: {averageCasual}")
        print(f"From {hour} to {hour + 6} average registered users: {averageRegistered}")
        print()

except IOError:
    print("The file is missing!")
