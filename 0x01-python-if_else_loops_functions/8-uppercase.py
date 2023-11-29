#!/usr/bin/python3
def uppercase(str):
    value = ord(str)
    if value >= 97 and value <= 122:
        return ''.join(chr(ord(value) - 32))
