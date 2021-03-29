import sys


def main():
    argc = len(sys.argv)
    Usage = "Usage: python operations.py <number1> <number2>"
    Example = "Example:\n\tpython operations.py 10 3"
    if (argc == 3):
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
        except:
            print("InputError: only numbers\n", Usage, Example, sep='\n')
            sys.exit(1)
        print("Sum: {}".format(a + b))
        print("Difference: {}".format(a - b))
        print("Product: {}".format(a * b))
        if (b == 0):
            print("ERROR (div by zero)")
            print("ERROR (div by zero)")
        else:
            print("Quotient: {}".format(a / b))
            print("Remainder: {}".format(a % b))
    if (argc > 3):
        print("InputError: too many arguments\n")
    if (argc > 3 or argc < 3):
        print(Usage, Example, sep='\n')


if __name__ == "__main__":
    main()