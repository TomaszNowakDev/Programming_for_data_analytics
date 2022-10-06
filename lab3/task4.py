# Lab 3 task 4

a = [1, 2, 3]
b = [4, 5, 6]
d = {}

if len(a) == len(b):
    for i in range(len(a)):
        d[a[i]] = b[i]
else:
    print("Length of lists doesn't match")

print(d)
