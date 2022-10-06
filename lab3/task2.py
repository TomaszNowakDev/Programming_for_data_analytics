# Lab 3 task2

def convert(lis):
    new_list_len = len(set(lis))
    len_lis = len(lis)
    return len_lis - new_list_len


a = [1, 2, 3, 4, 5, 3, 4, 5]
x = convert(a)

print(x)
