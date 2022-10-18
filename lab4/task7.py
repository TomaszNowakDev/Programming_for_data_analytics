# Lab 4 task 7
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    one_third = int(len(data)/3)

    section1 = data[:one_third, :]
    section2 = data[one_third:(2*one_third), :]
    section3 = data[2*one_third:, :]

    print(f"Average temperature and causal users section1: {format(np.mean(section1[:, 9]), '.2f')}"
          f"  {format(np.mean(section1[:, 13]), '.2f')} ")
    print(f"Average temperature and causal users section2: {format(np.mean(section2[:, 9]), '.2f')}"
          f"  {format(np.mean(section2[:, 13]), '.2f')} ")
    print(f"Average temperature and causal users section3: {format(np.mean(section3[:, 9]), '.2f')}"
          f"  {format(np.mean(section3[:, 13]), '.2f')} ")

    # observation the higher temperature more causal users

except IOError:
    print("Where is the data?")
