#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i + 1] > max:
            max = my_list[i]
    return max
