t = (3,30,2019,9,25)


def main():
    date = f"{t[3]:02}/{t[4]:02}/{t[2]:02}"
    time = f"{t[0]:02}:{t[1]:02}"
    print(date, time)


if __name__ == "__main__":
    main()