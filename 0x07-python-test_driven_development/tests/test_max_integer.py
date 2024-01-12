#!/usr/bin/python3
"""test max_integer module."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxTest(unittest.TestCase):
    """unit test."""
    def test_ordered_list(self):
        """ test ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unorderd_list(self):
        """test unordered."""
        self.assertEqual(max_integer([3, 2, 4, 3]), 4)

    def test_max_at_bigin(self):
        """max at the bigining."""
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_empty(self):
        """test empty."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """test one element."""
        self.assertEqual(max_integer([4]), 4)

    def test_float(self):
        """test flots."""
        self.assertEqual(max_integer([4.9, 1.9, 6.3, 3.8]), 6.3)

    def test_ints_floats(self):
        """test ints and floats."""
        self.assertEqual(max_integer([4.6, 1.65, 6.21, 3]), 6.21)

    def test_string(self):
        """test string."""
        self.assertEqual(max_integer("Hello"), 'o')
    
    def test_strings(self):
        """test strings."""
        self.assertEqual(max_integer(["My", "name", "is", "Erdey"]), "name")

    def test_empty_string(self):
        """test empty string."""
        self.assertEqual(max_integer(""), None)
