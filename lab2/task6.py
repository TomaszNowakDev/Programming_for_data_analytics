# Lab 2 task 6
import task6_modules

MENU = "Would you like to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n>"


def main():
    number1, number2 = task6_modules.get_numbers()

    choice = task6_modules.get_choice(MENU)

    while choice != 5:
        if choice == 1:
            result = task6_modules.addition(number1, number2)
            print(f"Addition of {number1} and {number2} is {result}\n")
        elif choice == 2:
            result = task6_modules.subtraction(number1, number2)
            print(f"Subtraction of {number1} and {number2} is {result}\n")
        elif choice == 3:
            result = task6_modules.multiplication(number1, number2)
            print(f"Multiplication of {number1} and {number2} is {result}\n")
        elif choice == 4:
            result = task6_modules.division(number1, number2)
            print(f"Division of {number1} and {number2} is {result}\n")

        number1, number2 = task6_modules.get_numbers()
        choice = task6_modules.get_choice(MENU)

    print("Thank you. Goodbye!")


if __name__ == '__main__':
    main()
