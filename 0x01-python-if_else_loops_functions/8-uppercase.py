#!/usr/bin/python3
def uppercase(str):
    for i in str:
        value = ord(str)
        if value >= 97 and value <= 122:
            i = chr(ord(i) - 32)
            print("{:s}".format(i), end="")
        print()
