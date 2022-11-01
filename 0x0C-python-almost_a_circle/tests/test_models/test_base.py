#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
import inspect
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the base class
    """

    @classmethod
    def setUpClass(cls):
        """creating a set up environment for testing
           documentation
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """to test if documentation for module is present
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """to test if documentation for class is present
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstring(self):
        """to test if documentation for function is present
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test__(self):
        """ a function to test id values
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
