# task8

import math

while True:
    try:
        radius = int(input("What is the radius of the circle? "))
        break
    except ValueError:
        print("Whole numbers only!")
area = math.pi * radius ** 2

print(format(area, '.2f'))
