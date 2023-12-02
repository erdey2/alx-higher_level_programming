#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    my_new_list = my_list[0:size]
    if (idx < 0):
        return my_new_list
    elif (idx >= size):
        return my_new_list
    else:
        my_new_list[idx] = element
    return my_new_list
