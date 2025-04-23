from fractions import Fraction

def readInt():
    try:
        return int(input("Enter an integer"))

    except ValueError as e:
        print(f"{e}: The value you entered cannot be converted to an integer. Returning None")
        return None


def readVal(valType, promptMsg, errorMsg):
    try:
        value = input(f"{promptMsg}: ")
        return valType(value)

    except ValueError as e:
        print(f"{value} {errorMsg}. Returning {value}")
        return value


def main():
    val = readVal(int, 'Enter an integer', 'is not an integer')
    print(val)
    val = readVal(float, 'Enter a float', 'is not a float')
    print(val)
    val = readVal(Fraction, 'Enter a fraction', 'is not a fraction')
    print(val)
    val = readVal(complex, 'Enter a complex number (e.g., 1+2j)', 'is not a valid complex number')
    print(val)

if __name__ == "__main__":
    main()


