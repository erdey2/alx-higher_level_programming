#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if (idx < 0):
        print('{:s}'.format('None'))
    elif (idx > size):
        print('{:s}'.format('None'))
    else:
        print('{:d}'.format(my_list[idx]))
