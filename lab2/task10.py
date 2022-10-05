# lab2 task 10

positive_numbers = 0
negative_numbers = 0
total_lines = 0
blank_lines = 0
words_count = 0
float_num = 0

try:
    book = open("PrideAndPrejudice.txt", 'r')
    line = " "

    while line != "":
        line = book.readline()
        total_lines += 1
        words = line.split()
        if line == "\n":
            blank_lines += 1
        for word in words:
            words_count += 1
            try:
                temp = int(word)
                if temp < 0:
                    negative_numbers += 1
                if temp > 0:
                    positive_numbers += 1
            except ValueError:
                try:
                    temp = float(word)
                    float_num += 1
                except ValueError:
                    words_count += 1
    book.close()
except IOError:
    print("File does not exist!")

print(f"Total lines: {total_lines}\nTotal words: {words_count}\nBlank lines: {blank_lines}\nPositive ints:"
      + f"{positive_numbers}\nNegative ints: {negative_numbers}\nFloats: {float_num}")
