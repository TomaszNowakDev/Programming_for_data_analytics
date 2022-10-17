# Lab 4 task 1
import numpy as np

np_array = np.arange(81, dtype=float).reshape(9, 9)
print(np_array)
print()

size = int(len(np_array))
size_third = int(size/3)
size_two_third = int(size_third * 2)

print(np_array[size_third:size_two_third, size_third:size_two_third])
