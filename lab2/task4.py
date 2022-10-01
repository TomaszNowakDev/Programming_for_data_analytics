def average(mon):
    rain_sum = 0
    highest = 0
    for i in range(mon):

        while True:
            try:
                rainfall = float(input(f"Who much rainfall in month {i+1 }>"))
                if rainfall >= 0:
                    break
            except ValueError:
                print("Enter number between 1 and 12!")
        if rainfall > highest:
            highest = rainfall

        rain_sum += rainfall
    return highest, rain_sum/mon


while True:
    try:
        months = int(input("Number of months >"))
        if 12 >= months > 0:
            break
    except ValueError:
        print("Check your data and start the program again!")


high, aver = average(months)
print(f"Highest rainfall value: {high}\nAverage is {aver}")
