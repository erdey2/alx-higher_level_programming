#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        size = len(my_list)
        for i in range(-1, -(size + 1), -1):
            print('{:d}'.format(my_list[i]))
