#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
sys.path.append('/root/alx-higher_level_programming' +
                '/0x07-python-test_driven_development')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 8]), 8)
        self.assertEqual(max_integer([8, 2, 1]), 8)
        self.assertEqual(max_integer([1, 8, 2]), 8)
        self.assertEqual(max_integer([1, 2, -8]), 2)
        self.assertEqual(max_integer([-1, -2, -8]), -1)
        self.assertEqual(max_integer([1, 8]), 8)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
