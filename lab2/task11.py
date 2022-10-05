# lab 2 task 11

try:
    book = open("PrideAndPrejudice.txt", 'r')
    long_lines = open("PrideAndPrejudiceHighlights.txt", 'w')
    line = " "

    while line != "":
        line = book.readline()
        words = line.split()
        if len(words) > 10:
            long_lines.write(line)

    book.close()
    long_lines.close()
except IOError:
    print("File does not exist!")
