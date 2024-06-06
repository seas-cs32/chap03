### chap03/import.py
print("import.py: At start of script")

import module32

def main():
    print("import.py: At start of main")

    print(f"i = {module32.i}; ")
    print(f"still42? {module32.still42()}")

print("import.py: Before check of __name__ =", __name__)
if __name__ == '__main__':
    main()