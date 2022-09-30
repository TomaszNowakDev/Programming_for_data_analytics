# task 6

A = 25
B = 20
C = 30


def main():
    tickets_a = 0
    tickets_b = 0
    tickets_c = 0
    try:
        tickets_a = int(input("How many Class A tickets? \n>>>"))
        tickets_b = int(input("How many Class B tickets? \n>>>"))
        tickets_c = int(input("How many Class C tickets? \n>>>"))
    except ValueError:
        print("Whole numbers only!")

    total = (A * tickets_a) + (B * tickets_b) + (C * tickets_c)
    print("Total income for tickets:", total, "euro.")


if __name__ == '__main__':
    main()
