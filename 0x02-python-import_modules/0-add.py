#!/usr/bin/python3
import add_0
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
res = add_0.add(a, b)
print('{:d} + {:d} = {:d}'.format(a, b, res))
