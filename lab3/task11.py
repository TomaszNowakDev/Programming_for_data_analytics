# Lab 3 task 11

class PassengersQuantity:

    def __init__(self, index, date, air_passengers):
        self.index = index
        self.date = date
        self.air_passengers = air_passengers

    def setData(self, date):
        self.date = date

    def setAirPassengers(self, air_passengers):
        self.air_passengers = air_passengers

    def getIndex(self):
        return self.index

    def getDate(self):
        return self.date

    def getAirPassengers(self):
        return self.air_passengers


def statistics(file_name):
    data_from_file = open(file_name, "r")

    my_data = []
    for line in data_from_file:
        split_line = line.split(",")
        index = int(split_line[0])
        qtr = float(split_line[1])
        quantity = int(split_line[2])
        quarter = PassengersQuantity(index, qtr, quantity)
        my_data.append(quarter)

    data_from_file.close()

    passengers_num = []

    for num in my_data:
        passengers_num.append(num.getAirPassengers())

    max_passengers = max(passengers_num)
    min_passengers = min(passengers_num)
    average = sum(passengers_num) / len(passengers_num)
    print(f"Max: {max_passengers}\nMin: {min_passengers}\nAverage: {average}")


statistics("AirPassengers.csv")
