import numpy as np


def even_second_half(arr):

    print(arr)
    print()

    second_half = int(len(arr[0])/2)
    print(arr[1::2, second_half:])


def main():
    array = np.array([[14.4, 2.4, 3.5, 5.3], [54.3, 34.4, 98.22, 65.4], [100, 200, 300, 400]], float)
    even_second_half(array)


if __name__ == '__main__':
    main()
