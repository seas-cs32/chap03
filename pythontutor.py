### chap03/pythontutor.py
def my_replace(s, old, new):
    i = 0            # tracks where we are in the input string
    j = len(old)     # skip-ahead amount for index calculations 
    new_s = s[0:0]   # the new string we're building 
 
    while i < len(s): 
        if s[i:i+j] == old: 
            new_s = new_s + new 
            i += j 
        else: 
            new_s = new_s + s[i:i+1] 
            i += 1 
 
    return new_s 
 
my_book =  [ 
    'And ...', 
    'The Cat in the Hat!', 
    ] 
while len(my_book) > 0: 
    the_line = my_book.pop(0) 
 
     # Having some fun with text substitution 
    the_line = my_replace(the_line, 'Cat', '\N{cat face with wry smile}') 
    the_line = my_replace(the_line, 'Hat', '\N{top hat}') 
 
    print(the_line) 
