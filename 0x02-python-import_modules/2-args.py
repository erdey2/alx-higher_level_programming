#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    size = len(sys.argv)
    size = size - 1
    if (size == 0):
        print('{:d} arguments.'.format(size))
    elif (size == 1):
        print('{:d} argument:'.format(size))
        print('{:d}: {}'.format(size, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(size))
        for i in range(size):
            print('{:d}: {}'.format(i + 1, sys.argv[i + 1]))
