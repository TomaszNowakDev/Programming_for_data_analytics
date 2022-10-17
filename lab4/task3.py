# Lab 4 task 3
import numpy as np


def read_bike_sharing(file_name):
    try:
        data = np.genfromtxt(file_name, dtype=float, delimiter=',')

        print(np.unique(data[:, 1]))

    except IOError:
        print("Where is the data?")


def main():
    read_bike_sharing('bikeSharing.csv')


if __name__ == '__main__':
    main()
