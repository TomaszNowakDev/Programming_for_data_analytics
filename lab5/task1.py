# Lab 5 task 1
import numpy as np
import random

arr = np.array([])

for i in range(100):
    arr = np.append(arr, random.randint(1, 100))

arr[arr % 2 == 1] = -1

arr[arr % 2 == 0] += arr[arr % 2 == 0] + 1

print(arr)
