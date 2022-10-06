# Lab 3 task 1

students = {}

while True:
    try:
        num = int(input("How many numbers >"))
        break
    except ValueError:
        print("Whole numbers only!")

for i in range(num):
    name = input(f"Please enter the student name {i+1}: ")
    student_id = input(f"Please enter the student ID {name}: ")
    if not student_id.isdigit():
        student_id = input(f"Please enter the student ID {name}: ")
    else:
        students[student_id] = name
