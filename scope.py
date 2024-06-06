### chap03/scope.py
capitalize = True   # a global variable setting a mode for the script

def my_print(s):
    if capitalize:
        s = s.capitalize()
    print(s)

def my_scramble(s):
    new_s = s[1:] + s[0]
    return new_s

s = 'just some fun'
my_print(s)
print(my_scramble(s))
#print(new_s)  # produces a NameError