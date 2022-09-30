# task 5

weight = int(input("What is your weight(in pounds)? \n>>>"))
height = int(input("What is your height(in inches)? \n>>>"))

bmi = ((weight/(height**2))*703)

print("Your BMI is", format(bmi, '.2f'))
