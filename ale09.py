### chap03/ale09.py
def my_replace(s, old, new):
    i = 0           # tracks where we are in the input string
    j = len(old)    # skip-ahead amount for index calculations
    new_s = s[0:0]  # the new string we're building

    while i < len(s):
        if s[i:i+j] == old:
            new_s = new_s + new
            i += j
        else:
            new_s = new_s + s[i:i+1]
            i += 1

    return new_s

def main():
    s = 'Learning never exhausts the mind. Leonardo da Vinci'
    soln1 = 'Learning never exhausts the 🧠. Leonardo da Vinci'
    soln2 = 'Learning never exhausts the mind. Leonardo da VINCI'

    # Check a replacement in the input string
    s_new = my_replace(s, 'mind', '\N{brain}')
    print(s_new)
    assert s_new == soln1, "my_replace didn't work correctly"

    # Check a replacement at the end of the input string
    s_new = my_replace(s, 'Vinci', 'VINCI')
    print(s_new)
    assert s_new == soln2, "my_replace didn't work correctly"

if __name__ == '__main__':
    main()
