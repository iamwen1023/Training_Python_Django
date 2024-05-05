def numbers():
    f = open("numbers.txt", "r")
    f_read = f.read()
    f_split = f_read.split(",")
    for x in f_split:
        print(x.strip())
    f.close()


if __name__ == '__main__':
    numbers()