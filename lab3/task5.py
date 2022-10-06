# Lab 3 task 5

import random


def create_dictionary():
    new_dictionary = {}
    for i in range(10):
        new_dictionary[i+1] = random.randint(1, 20)

    list_keys = new_dictionary.keys()
    list_values = new_dictionary.values()
    print(list_keys, list_values)


create_dictionary()
