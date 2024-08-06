### chap03/replace23.py
my_book = input('What book would you like to read? ')
print()   # print a blank line between question and script's output

with open('txts/' + my_book) as my_open_book:
    while True:
        the_line = my_open_book.readline()

        # Having some fun with text substitution
        #the_line = the_line.replace('Cat', '\u0047')
        #the_line = the_line.replace('Cat', '\U0001F63C')
        the_line = the_line.replace('Cat', '\N{cat face with wry smile}')

        print(the_line, end='')

        # Check for EOF
        if the_line == '':
            break

print("\nThe End.")
