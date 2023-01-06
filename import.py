### chap03/import.py

print(f"{__name__}: Before the import in import.py")
import module32
print(f"{__name__}: After the import in import.py")

def main():
    print(f"{__name__}: In main of import.py; ", end='')
    print(f"i = {module32.i}; ", end='')
    print(f"still42? {module32.still42()}")

if __name__ == '__main__':
    main()