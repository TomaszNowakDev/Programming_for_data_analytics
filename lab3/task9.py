# lab3 task 9

def add_name():
    my_list = []
    cont = 'y'
    while cont == 'y':
        name = input("name")
        my_list.append(name)
        cont = input("[y/n]?")
    my_tuple = tuple(my_list)
    return my_tuple
        