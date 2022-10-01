# Lab 2 Task 1
TAX_RATE1 = .35
TAX_RATE2 = .4
TAX_RATE3 = .45
TAX_RATE4 = .5
TAX_RATE5 = .55

salary = 0
kids = "n"


def count_tax(sal, rate):
    return sal * rate


while True:
    try:
        salary = float(input("What is your salary? "))
        if salary >= 0:
            break
    except ValueError:
        print("Numbers only!")

if 30 <= salary <= 70:
    kids = input("Do you have kids?[y/n] ").lower()

    if 30 <= salary < 50 and kids == "y":
        tax = count_tax(salary, TAX_RATE1)
        print("Tax to pay:", tax)
    elif 30 <= salary < 50 and kids == "n":
        tax = count_tax(salary, TAX_RATE2)
        print("Tax to pay:", tax)
    elif 50 <= salary <= 70 and kids == "y":
        tax = count_tax(salary, TAX_RATE3)
        print("Tax to pay:", tax)
    elif 50 <= salary <= 70 and kids == "n":
        tax = count_tax(salary, TAX_RATE4)
        print("Tax to pay:", tax)

elif salary > 70:
    tax = count_tax(salary, TAX_RATE5)
    print("Tax to pay:", tax)
else:
    print("You are not paying any tax on your salary!")
