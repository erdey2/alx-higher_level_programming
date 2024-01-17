#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test rectangle."""
    test_area_positive(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1, 6)

    
    test_area_negative(self):
        r2 = Rectangle(-3, -2)
        self.assertEqual(r2, 6)

    test_area_empty(self):
        r3 = Rectangle()
        self.assertEqual(r3, 0)
    
    test_area_string(self):
        r4 = Rectangle('-3', 2)
        self.assertEqual(r4, '-3-3')
