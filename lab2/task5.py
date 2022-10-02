# Lab2 task 5
def q5(n):
    next_fib = 0
    fib0 = 0
    fib1 = 1
    for i in range(2, n):
        next_fib = fib0 + fib1
        fib0 = fib1
        fib1 = next_fib
    print(next_fib)


def get_fib(inx):
    return q5(inx - 1)


x = -1
try:
    x = int(input("Enter positive integer\n>"))
except ValueError:
    print("Wrong data")

get_fib(x)
