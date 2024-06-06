### chap03/module32.py
print("module32.py: At start of script")

# Initialize a variable in this module
i = 42
print("module32.py: Initialized i")

def still42():
    return i == 42

def main():
    print("module32.py: At start of main")

print("module32.py: Before check of __name__ =", __name__)
if __name__ == '__main__':
    main()