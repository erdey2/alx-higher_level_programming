#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique = set(my_list)
    my_list2 = list(unique)
    for i in range(len(my_list2)):
        sum += my_list2[i]
    return sum
