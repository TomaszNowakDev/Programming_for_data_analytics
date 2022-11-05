# Lab 5 task 7
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')
    for temp in range(1, 40, 5):
        # the temperature values stored in the array are multiplied by 41
        minValue = temp
        maxValue = temp + 4
        higherTempCondition = (data[:, 9] * 41) >= minValue

        lowerTempCondition = (data[:, 9] * 41) <= maxValue

        subset = data[higherTempCondition & lowerTempCondition]

        meanValue = np.mean(subset[:, 13])

        print(f"For temp in range {minValue} to {maxValue}, mean casual is {format(meanValue,'.2f')}")


except IOError:
    print("The file is missing!")
