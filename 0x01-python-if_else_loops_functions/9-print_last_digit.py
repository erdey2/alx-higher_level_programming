#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = (-1 * number) % 10
    elif number > 0:
        last_num = number % 10
    else:
        last_num = 0
    print('{:d}'.format(last_num), end='')
    return last_num
