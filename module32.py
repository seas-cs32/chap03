### chap03/module32.py

# Initialize a variable in this module
i = 42
print(f"{__name__}: Initialized i in module32.py")

def still42():
    return i == 42

def main():
    print(f"{__name__}: In main of module32.py")

if __name__ == '__main__':
    main()