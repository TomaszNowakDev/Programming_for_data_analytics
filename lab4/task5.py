# Lab 4 task 5
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

# new data holds improved data
    new_data = np.copy(data)
    new_data[:, 9] *= 41
    new_data[:, 10] *= 50
    new_data[:, 11] *= 100
    new_data[:, 12] *= 67
    print(new_data[:, 9:13])
    print()

# new array just for improved temperatures
    new_array = data[:, 9:13]

    new_array[:, 0] *= 41
    new_array[:, 1] *= 50
    new_array[:, 2] *= 100
    new_array[:, 3] *= 67

    print(new_array)

except IOError:
    print("Where is the data?")
