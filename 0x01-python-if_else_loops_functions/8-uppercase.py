#!/usr/bin/python3


def uppercase(str):
    """a function that prints a string in uppercase
       followed by a new line.
    """
    new = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            new += chr(ord(i)-32)
        else:
            new += i
    print("{}".format(new), end="\n")
