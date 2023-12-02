#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list == []:
        return 0
    else:
        for i in my_list:
            my_list = print('{:d}'.format(i))
        return my_list
