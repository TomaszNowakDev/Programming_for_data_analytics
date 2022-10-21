# Lab 4 task 10

import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    new_data = np.delete(data, 0, axis=1)

    np.savetxt("minusFirstColumnBike.csv", new_data, delimiter=',', fmt='%.2f')


except IOError:
    print("Couldn't find the file")
