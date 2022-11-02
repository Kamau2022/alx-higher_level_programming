#!/usr/bin/python3
"""a unnitest"""

import unittest
import sys
import io
import contextlib
import inspect
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """a class to carry out various tests
    """

    @classmethod
    def setUpClass(cls):
        """Creating a set up environment for testing
        """
        cls.r1 = Rectangle(2, 10)
        cls.r2 = Rectangle(2, 4)
        cls.r3 = Rectangle(6, 7, 8)
        cls.r4 = Rectangle(6, 7, 8, 9)
        cls.r5 = Rectangle(2, 9, 0, 43, 77)
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """Test if module documentation is present
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Test if class documentation is present
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstring(self):
        """Test if function documentation is present
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_init_values(self):
        """a function to test id values
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 4)
        self.assertEqual(self.r5.id, 77)

    def test_width_values(self):
        """a function to test width values
        """
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 6)
        self.assertEqual(self.r4.width, 6)
        self.assertEqual(self.r5.width, 2)

    def test_height_values(self):
        """a function to test height values
        """
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r3.height, 7)
        self.assertEqual(self.r4.height, 7)
        self.assertEqual(self.r5.height, 9)

    def test_x_values(self):
        """a function to test x values
        """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 8)
        self.assertEqual(self.r4.x, 8)
        self.assertEqual(self.r5.x, 0)

    def test_y_values(self):
        """a function to test y values
        """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r4.y, 9)
        self.assertEqual(self.r5.y, 43)

    def test_height_errors(self):
        """a function to test height errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 'g')
        with self.assertRaises(TypeError):
            r = Rectangle(1, [4, 5])
        with self.assertRaises(TypeError):
            r = Rectangle(1, (4, 5))
        with self.assertRaises(TypeError):
            r = Rectangle(1, {"ben": 23, "john": 34})
        with self.assertRaises(TypeError):
            r = Rectangle(1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2.5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_width_errors(self):
        """a function to test width errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle("g", 1)
        with self.assertRaises(TypeError):
            r = Rectangle([4, 5], 1)
        with self.assertRaises(TypeError):
            r = Rectangle({"ben": 23, "john": 34}, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(2.5, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 1)

    def test_x_errors(self):
        """a function to test x errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "g")
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, [4, 5])
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, {"ben": 23, "john": 34})
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 2.5, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -2, 1)

    def test_y_errors(self):
        """a function to test y errors
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "g", 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, [4, 5], 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, {"ben": 23, "john": 34}, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 2.5, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -2, 1)

    def test_other_errors(self):
        """a function to test other possible errors
        """
        with self.assertRaises(TypeError):
            p = Rectangle()
        with self.assertRaises(TypeError):
            p = Rectangle(1)
        with self.assertRaises(TypeError):
            p = Rectangle(None)
        with self.assertRaises(TypeError):
            p = Rectangle(1, 2, 3, 4, 5, 6)

    def test_area(self):
       """a function to test values for area 
       """
       self.assertEqual((self.r1.width * self.r1.height), 20)
       self.assertEqual((self.r2.width * self.r2.height), 8)
       self.assertEqual((self.r3.width * self.r3.height), 42)
       self.assertEqual((self.r4.width * self.r4.height), 42)
       self.assertEqual((self.r5.width * self.r5.height), 18)

    def test_area_errors(self):
        """a function to test errors i finding area
        """
        with self.assertRaises(TypeError):
            a = Rectangle()
        with self.assertRaises(TypeError):
            a = Rectangle(1)
        with self.assertRaises(ValueError):
            a = Rectangle(-1, 4)   
   
    def test_display(self):
        """a function to test the display method
        """
        j = io.StringIO()
        with contextlib.redirect_stdout(j):
            self.r2.display()
        k = j.getvalue()
        self.assertEqual(k, "##\n##\n##\n##\n")









