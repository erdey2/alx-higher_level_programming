#!/usr/bin/python3
"""Custom int implementation."""


class MyInt(int):
    """MyInt implementation."""
    def __init__(self, value):
        """Initialize instances."""
        self.__value = value

    def __eq__(self, value):
        """convert equals to not equal."""
        return self.__value != value

    def __ne__(self, value):
        """convert not equal to equal."""
        return self.__value == value
