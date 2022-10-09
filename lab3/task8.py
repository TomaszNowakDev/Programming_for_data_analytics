# Lab 3 task 8

def get_int(lis):
    new_list = []
    my_set = set(lis)
    for i in my_set:
        if type(i) == int:
            new_list.append(i)
    print(new_list)


get_int([1, 2, "Tomasz", 2.54, '3', 1, 4, 5, 6])
