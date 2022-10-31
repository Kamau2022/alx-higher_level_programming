#!/usr/bin/python3
"""a unnitest"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """a class to carry out various tests"""
    def test_init_values(self):
        """a function to height and width values"""
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 4)
