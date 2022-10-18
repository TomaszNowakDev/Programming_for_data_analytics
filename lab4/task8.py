# Lab 4 task 8
import numpy as np

try:
    data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter=',')

    np_list = []
    # calculating number of np arrays
    nps_num = int(len(data)/1000)

    # dividing data into chunks of 1000 records
    for i in range(nps_num):
        dataset = np.copy(data[(i*1000):(i+1)*1000, :])
        np_list.append(dataset)

    for i in np_list:
        print(f"Average feeling temperature and causal users for section: {format(np.mean(i[:, 9]), '.2f')}"
              f"  {format(np.mean(i[:, 13]), '.2f')} ")

except IOError:
    print("Where is the data?")
