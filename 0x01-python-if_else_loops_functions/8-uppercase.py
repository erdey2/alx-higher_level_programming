#!/usr/bin/python3
def uppercase(str):
    value = ord(str)
    if value >= 97 and value <= 122:
        value = chr(value) - 32
    print("{}".format(value))