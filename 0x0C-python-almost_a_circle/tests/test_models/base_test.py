#!/usr/bin/python3
"""test base.py module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    test_to_json_string(self):
        self.assertEqual([{'id':1}]
