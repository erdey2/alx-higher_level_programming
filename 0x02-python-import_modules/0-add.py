#!/usr/bin/python3
import add_0
import sys
def main():
    a = 1
    b = 2
    res = add_0.add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, res))

if __name__ == '__main__':
    main()
