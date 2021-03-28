import sys
argc = len(sys.argv)
if(argc > 1):
    string = sys.argv[1]
    i = 2
    while(i < argc):
        string += ' '
        string += sys.argv[i]
        i += 1
    reverse = string[::-1]
    print(reverse.swapcase())
