import sys


def main():
    s = ' '.join(sys.argv[1::])
    print(s.swapcase()[::-1])


if __name__ == "__main__":
    main()