### chap03/replace4.py
my_book = input('What book would you like to read? ')
print()   # print a blank line between question and script's output

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        the_line = the_line.replace('Cat', '\N{cat face with wry smile}')
        the_line = the_line.replace('Hat', '\N{top hat}')

        print(the_line, end='')

        # Check for EOF
        if the_line == '':
            break

print("\nThe End.")
