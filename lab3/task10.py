# lab 3 task 10

def clean_data(check_word):
    delete_list = ".,:;()[]?‘\"-_\\|"
    for symbol in delete_list:
        if symbol in check_word:
            check_word = check_word.replace(symbol, "")
    return check_word


try:
    book = open("SherlockHolmes.txt", 'r')
    line = " "
    characterLength = 10
    upperFreq = 5
    dict1 = {}
    new_list = []
    book_text = book.read()
    book.close()
    words = book_text.split()
    for word in words:
        word = clean_data(word)
        if len(word) == characterLength:
            if word not in dict1:
                dict1[word] = 1
            else:
                dict1[word] += 1

    for key in dict1:
        if dict1[key] <= upperFreq:
            new_list.append(key)

    print(new_list)

except IOError:
    print("where is the book?")


