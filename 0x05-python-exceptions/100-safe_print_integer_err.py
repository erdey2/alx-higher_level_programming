#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as error:
        print(f'Exception {error}', file=sys.stderr)
