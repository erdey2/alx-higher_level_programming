#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except ZeroDivisionError, TypeError, ValueError, IndexError as error:
        result = None
        print(f'Exception {error}', file=sys.stderr)
    return result
