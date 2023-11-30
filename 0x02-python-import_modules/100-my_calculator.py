#!/usr/bin/python3

if (__name__ == '__main__'):
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv)
    if (argc != 4):
        print('Usage:{} {} {} {}'.format(argv[0], '<a>', 'operator', '<b>'))
        sys.exit(1)
    op = argv[2]
    if (op == '+' or op == '-' or op == '*' or op == '/'):
        if (op == '+'):
            summ = add(int(argv[1]), int(argv[3]))
            print('{:s} + {:s} = {:d}'.format(argv[1], argv[3], summ))
        elif (op == '-'):
            sub = sub(int(argv[1]), int(argv[3]))
            print('{:s} - {:s} = {:d}'.format(argv[1], argv[3], sub))
        elif (op == '*'):
            mul = mul(int(argv[1]), int(argv[3]))
            print('{:d} * {:d} = {:d}'.format(argv[1], argv[3], mul))
        elif (op == '/'):
            div = div(int(argv[1]), int(argv[3]))
            print('{:s} / {:s} = {:d}'.format(argv[1], argv[3], div))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
