#!/usr/bin/python3
"""a program that defines attributes of a rectangle"""


class Rectangle:
    """a class that defines a rectangle"""
    def __init__(self, __width=0, __height=0):
        self.__height = __height
        self.__width = __width

    @property
    def width(self):
        """a function that retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a function that sets the value of width"""
        if not(isinstance(value, (int))):
            raise ValueError("width must be an integer")
        self.__width = value
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a function that retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a function that sets value of height"""
        if not(isinstance(value, (int))):
            raise ValueError("height must be an integer")
        self.__height = value
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
