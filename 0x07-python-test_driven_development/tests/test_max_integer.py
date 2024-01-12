#!/usr/bin/python3
"""test max_integer module."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxTest(unittest.TestCase):
    """unit test."""
    def testMaximum(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)
        self.assertEqual(max_integer([4, 6, 1, 3]), 6)
        self.assertEqual(max_integer([4, 1, 6, 3]), 6)
        self.assertEqual(max_integer([4, -6, -1, -3]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -1, -3]), -1)
