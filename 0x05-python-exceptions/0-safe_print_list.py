#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(mylist[i], end='')
            count += 1
        except IndexError:
            continue
    print()
    return count
