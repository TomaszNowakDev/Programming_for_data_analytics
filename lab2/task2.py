# Lab 2 task 2

salary40 = False
age25 = False
work25 = True
kid = True

# part A
if (salary40 and age25) or (work25 and kid):
    print("Mortgage approved")
else:
    print("Mortgage denied")

# part B

salary40 = False
age35 = False
work10 = True
kid = True

if (salary40 or age35) and (work10 or kid):
    print("Mortgage approved")
else:
    print("Mortgage denied")
