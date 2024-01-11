#!/usr/bin/python3
"""MyList class implementation."""


class MyList(list):
    """print sorted list."""
    def print_sorted(self):
        """print list in asending order."""
        copy_list = self[:]
        copy_list.sort()
        print(copy_list)
