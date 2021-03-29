import sys


def main():
    if (len(sys.argv) == 2):
        arg = sys.argv[1]
        if arg.isdigit():
            if(int(arg) == 0):
                print("I'm Zero.")
            elif(int(arg) % 2 == 0):
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            print("ERROR")
    elif(len(sys.argv) > 2):
        print("ERROR")

if __name__ == "__main__":
    main()