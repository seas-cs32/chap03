### chap03/replace6.py

# specify the interface for my_replace
#     specify the implementation of my_replace

my_book = input('What book would you like to read? ')
print()   # print a blank line between question and script's output

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        # call my_replace on the_line, specifying 'Cat' is replaced by '\N{cat face with wry smile}'
        # call my_replace on the_line, specifying 'Hat' is replaced by '\N{top hat}'

        print(the_line, end='')

        # Check for EOF
        if the_line == '':
            break

print("\nThe End.")
