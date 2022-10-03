# task 7

def prime_check(n, i):
    if n <= 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime_check(n, i + 1)


x = 0
try:
    x = int(input("Enter an integer\n>"))
except ValueError:
    print("Whole numbers only please!!")

print(prime_check(x, 2))

