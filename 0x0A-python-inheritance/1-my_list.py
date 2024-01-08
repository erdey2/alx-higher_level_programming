#!/usr/bin/python3
"""MyList class implementation."""

class MyList(list):
    """print sorted list."""
    def print_sorted(self):
        print(sorted(self))
