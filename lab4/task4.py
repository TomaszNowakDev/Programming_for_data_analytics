# Lab 4 task 4
import numpy as np


def read_max_min_mean(file_name):
    try:
        data = np.genfromtxt(file_name, dtype=float, delimiter=',')
        print(f"Max temperature was: {np.max(data[:, 9])*41}\u00B0C")
        print(f"Min temperature was: {format(np.min(data[:, 9])*41, '.2f')}\u00B0C")
        print(f"Average temperature was: {format(np.mean(data[:, 9])*41, '.2f')}\u00B0C")

    except IOError:
        print("Where is the data?")


def main():
    read_max_min_mean('bikeSharing.csv')


if __name__ == '__main__':
    main()
