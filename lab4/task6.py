# Lab 4 task 6
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    one_third = int(len(data)/3)

    section1 = data[:one_third, :]
    section2 = data[one_third:(2*one_third), :]
    section3 = data[2*one_third:, :]

    new_array = np.append(section1, section3, axis=0)

    np.savetxt("newBike.csv", new_array, fmt='%.2f', delimiter=',')


except IOError:
    print("Where is the data?")
