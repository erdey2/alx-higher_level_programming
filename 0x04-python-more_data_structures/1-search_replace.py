#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            list2.append(replace)
        else:
            list2.append(my_list[i])
    return list2
