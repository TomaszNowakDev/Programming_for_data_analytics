# Lab 3 task 7

def get_int(lis):
    new_list = []
    for i in lis:
        if type(i) == int:
            new_list.append(i)
    print(new_list)


get_int([1, 2, "Tomasz", 2.54, '3', 1, 4, 5, 6])
