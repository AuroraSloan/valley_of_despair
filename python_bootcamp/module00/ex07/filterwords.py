import sys, re

def filterwords(mystr, num):
    mystr = re.sub(r'[^\w\s]','',mystr)
    mystr = [word for word in mystr.split(' ')]
    mystr = [i for i in mystr if len(i) > int(num)]
    print (mystr)


if __name__ == "__main__":
    filterwords(sys.argv[1], sys.argv[2])
