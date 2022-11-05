# Lab 5 task 6
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    print(f"Average number of bikes is {np.mean(data[:, 15])}")

    clear = data[data[:, 8] == 1]
    print(f"Average bikes for condition Clear is { np.mean(clear[:, 15])}")
    misty = data[data[:, 8] == 2]
    print(f"Average bikes for condition Misty is {np.mean(misty[:, 15])}")
    light_rain = data[data[:, 8] == 3]
    print(f"Average bikes for condition Clear is {np.mean(light_rain[:, 15])}")
    heavy_rain = data[data[:, 8] == 4]
    print(f"Average bikes for condition Heavy Rain is {np.mean(heavy_rain[:, 15])}")
    print()

# better way
    conditions = {1: "Clear", 2: "Misty", 3: "Light Rain", 4: "Heavy Rain"}
    for key in conditions:
        subsetData = data[data[:, 8] == key]
        print(conditions[key], np.mean(subsetData[:, 15]))

except IOError:
    print("The file is missing!")
