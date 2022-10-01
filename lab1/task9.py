# task9

G = 9.8
while True:
    try:
        mass1 = int(input("What is the mass of first object(in kg)? \n>>>"))
        mass2 = int(input("What is the mass of second object(in kg)?\n>>>"))
        distance = int(input("what is the distance between those two objects(in meters)? \n>>>"))
        break
    except ValueError:
        print("Whole numbers only!")

newtons = G * ((mass1 * mass2) / distance ** 2)
print(format(newtons, '.2f'))
