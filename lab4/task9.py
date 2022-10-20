# Lab 4 task 9

import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    new_column = data[:, 14] - data[:, 13]
    print(new_column)
    # reshaping (name of list, (num of rows, num of columns))
    new_column = np.reshape(new_column, (len(data), 1))

    data = np.append(data, new_column, axis=1)
    print(data)

    np.savetxt("newColumnBike.csv", data, delimiter=',', fmt='%.2f')

except IOError:
    print("Couldn't find the file.")
