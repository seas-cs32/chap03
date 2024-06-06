### chap03/scope_broken.py
capitalize = True   # a global variable setting a mode for the script

def my_print():
    if capitalize:
        s = s.capitalize()
    print(s)

def my_scramble():
    new_s = s[1:] + s[0]
    return new_s

s = 'just some fun'
my_print()
print(my_scramble())