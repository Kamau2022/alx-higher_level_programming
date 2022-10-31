#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test__init__(self, *args, **kwargs):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
