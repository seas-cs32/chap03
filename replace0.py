### chap03/replace0.py
my_book = input('What book would you like to read? ')
print()   # print a blank line between question and script's output

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()
        print(the_line, end='')

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break
