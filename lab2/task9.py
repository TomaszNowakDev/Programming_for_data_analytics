# Lab 2 task 9
import math

while True:
    try:
        x = int(input("Enter value for X coordinate >"))
        y = int(input("Enter value for Y coordinate >"))
        break
    except ValueError:
        print("Whole numbers only!")

ecl = math.hypot(x, y)
print(f"Euclidean distant: {ecl}")
