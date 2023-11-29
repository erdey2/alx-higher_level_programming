#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = (-1 * number) % 10
    else:
        last_num = number % 10
    print('{:d}'.format(last_num), end='')
