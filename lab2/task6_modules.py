# Basic maths operation

def get_numbers():
    while True:
        try:
            number1 = float(input("Please enter first number >"))
            number2 = float(input("Please enter second number >"))
            break
        except ValueError:
            print("Numeric values only!")
    return number1, number2


def get_choice(menu):
    while True:
        try:
            cho = int(input(menu))
            if 0 < cho < 6:
                break
            else:
                print("Select option from 1 to 5:")
        except ValueError:
            print("Whole numbers between 1 and 5 please!")
    return cho


def addition(num1, num2):
    return num1+num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Zero Division Error!"
    else:
        return num1 / num2
