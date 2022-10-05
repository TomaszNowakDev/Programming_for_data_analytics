# modules needed to task 8

def get_numbers():
    numbers = []
    while True:
        try:
            num = int(input("How many numbers >"))
            break
        except ValueError:
            print("Whole numbers only!")
    for i in range(num):
        while True:
            try:
                number = float(input(f"Enter number {i+1} \n>"))
                break
            except ValueError:
                print("Whole numbers only!")
        numbers.append(number)
    return numbers


def average_list(numbers):
    return sum(numbers)/len(numbers)


def sum_list(numbers):
    return sum(numbers)
