# lab 2 task 8
import task8_modules as func


def main():
    numbers = func.get_numbers()
    print(f"Average is: {func.average_list(numbers)}")
    print(f"Sum is: {func.sum_list(numbers)}")
    print(f"Max number is: {max(numbers)}")
    print(f"Min number is: {min(numbers)}")
    print(f"Sorted list form max to min: {sorted(numbers, reverse=True)}")
    print(f"Original list: {numbers}")


if __name__ == '__main__':
    main()
