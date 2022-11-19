#!/usr/bin/python3
"""a unnitest"""

import unittest
import sys
import io
import contextlib
import inspect
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """a class to carry out various tests
    """

    @classmethod
    def setUpClass(cls):
        """Creating a set up environment for conducting
           square values and doc tests
        """
        cls.s1 = Square(2)
        cls.s2 = Square(4)
        cls.s3 = Square(2, 4)
        cls.s4 = Square(6, 7, 8)
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """Test if module documentation is present
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """Test if class documentation is present
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstring(self):
        """Test if function documentation is present
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_subclass(self):
        """tests if Square is a subclass of Rectangle
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_init_values(self):
        """a function to test id values
        """
        self.assertEqual(self.s1.id, 31)
        self.assertEqual(self.s2.id, 32)
        self.assertEqual(self.s3.id, 33)
        self.assertEqual(self.s4.id, 34)

    def test_size_values(self):
        """a function to test height values
        """
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s4.size, 6)

    def test_x_values(self):
        """a function to test x values
        """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.x, 4)
        self.assertEqual(self.s4.x, 7)

    def test_y_values(self):
        """a function to test y values
        """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 0)
        self.assertEqual(self.s4.y, 8)

    def test_attrs(self):
        """ a fuction to test if the attributes are correctly set
        """
        self.assertEqual(self.s4.width, 6)
        self.assertEqual(self.s4.height, 6)
        self.assertEqual(self.s4.x, 7)
        self.assertEqual(self.s4.y, 8)

    def test_size_errors(self):
        """a function to test size errors
        """
        with self.assertRaises(TypeError):
            s = Square(1, 'g')
        with self.assertRaises(TypeError):
            s = Square(1, [4, 5])
        with self.assertRaises(TypeError):
            s = Square(1, (4, 5))
        with self.assertRaises(TypeError):
            s = Square(1, {"ben": 23, "john": 34})
        with self.assertRaises(TypeError):
            s = Square(1, None)
        with self.assertRaises(TypeError):
            s = Square(1, 2.5)
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_x_errors(self):
        """a function to test x errors
        """
        with self.assertRaises(TypeError):
            s = Square(1, 2, "g")
        with self.assertRaises(TypeError):
            s = Square(1, 2, [4, 5])
        with self.assertRaises(TypeError):
            s = Square(1, 2, {"ben": 23, "john": 34})
        with self.assertRaises(TypeError):
            s = Square(1, 2, None, 1)
        with self.assertRaises(TypeError):
            s = Square(1, 2, 2.5, 1)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -2, 1)

    def test_y_errors(self):
        """a function to test y errors
        """
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, "g", 1)
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, [4, 5], 1)
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, {"ben": 23, "john": 34}, 1)
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, None, 1)

    def test_other_errors(self):
        """a function to test other possible errors
        """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5, 6)

    def test_area(self):
        """a function to test values for area
        """
        self.assertEqual((self.s1.size * self.s1.size), 4)
        self.assertEqual((self.s2.size * self.s2.size), 16)
        self.assertEqual((self.s3.size * self.s3.size), 4)
        self.assertEqual((self.s4.size * self.s4.size), 36)

    def test_area_errors(self):
        """a function to test errors in finding area
        """
        with self.assertRaises(TypeError):
            a = Square()
        with self.assertRaises(ValueError):
            a = Square(-1, 4)

    def test_1_update_display(self):
        """a function to update the display method
        """
        j = io.StringIO()
        with contextlib.redirect_stdout(j):
            self.s3.display()
        k = j.getvalue()
        self.assertEqual(k, '    ##\n    ##\n')

    def test_str_method(self):
        """a function to test the __str__ method
        """
        self.assertEqual("[Square] (31) 0/0 - 2", str(self.s1))
        self.assertEqual("[Square] (32) 0/0 - 4", str(self.s2))
        self.assertEqual("[Square] (33) 4/0 - 2", str(self.s3))
        self.assertEqual("[Square] (34) 7/8 - 6", str(self.s4))

    def test_update_args(self):
        """a function to test the args a list of arguments:*args
        """
        s = Square(3, 5, 6, 7)
        s.update(13, 12, 11, 10)
        self.assertEqual(s.size, 12)
        self.assertEqual(s.x, 11)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.id, 13)

    def test_update_kwargs(self):
        """a function to test keyworded arguments:**kwargs
        """
        s = Square(3, 5, 6, 7)
        s.update(id=67, size=8, x=16, y=17)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.id, 67)
        self.assertEqual(s.x, 16)
        self.assertEqual(s.y, 17)

    def test_to_dictionary(self):
        """a test for the dictionary method
        """
        s = Square(10, 20, 30, 40)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict['size'], 10)
        self.assertEqual(s_dict['x'], 20)
        self.assertEqual(s_dict['y'], 30)
        self.assertEqual(s_dict['id'], 40)
