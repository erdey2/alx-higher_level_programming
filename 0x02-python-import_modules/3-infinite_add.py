#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    argc = len(sys.argv)
    argc = argc - 1
    res = 0
    if (argc == 0):
        res = 0
        print('{:d}'.format(res))
    elif argc == 1:
        res = int(sys.argv[1])
        print('{:d}'.format(res))
    else:
        for i in range(argc):
            res = res + int(sys.argv[i + 1])
        print('{:d}'.format(res))
