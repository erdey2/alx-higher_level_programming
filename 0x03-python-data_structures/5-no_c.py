#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    size = len(my_string)
    for i in range(size):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string += ''
        else:
            new_string += my_string[i]
    return new_string
