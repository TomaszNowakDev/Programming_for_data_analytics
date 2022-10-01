# Lab 2 task 3

def cal(n, ln):
    for i in range(ln+1):
        print(f"{n}*{i} = {n*i}")


def print_num_triangle(number):
    for i in range(number + 1):
        for j in range(i):
            print(i, end="")
        print()


def main():
    while True:
        try:
            num = int(input("Please enter time tables for printing >"))
            limit = int(input("Please enter upper limit for multiplication >"))
            if num >= 0 and limit >= 0:
                break
        except ValueError:
            print("Whole numbers only!")

    cal(num, limit)

    # part B
    print("\nPart B")

    while True:
        try:
            num1 = int(input("Please enter integer >"))
            if 10 > num1 > 0:
                break
        except ValueError:
            print("Whole numbers only!")

    print_num_triangle(num1)


if __name__ == '__main__':
    main()
