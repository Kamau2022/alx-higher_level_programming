#!/usr/bin/python3
"""a module showcasing attributes of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """a class that describes attributes of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """a class constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not(isinstance(self.__width, (int))):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        if not(isinstance(self.__height, (int))):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
        if not(isinstance(self.__y, (int))):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        if not(isinstance(self.__x, (int))):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    @property
    def width(self):
        """a function that retrieves width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """a function that sets the value of width
        Args:
             width: value of width
        """
        if not(isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
            self.__width = width

    @property
    def height(self):
        """a function that retrieves height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """a function that sets value of height
        Args:
            height: value of height
        """
        if not(isinstance(height, int)):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
            self.__height = height

    @property
    def x(self):
        """a function that retrieves x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """a function that sets the value of x
        Args:
            x: value of x
        """
        if not(isinstance(x, int)):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
            self.__x = x

    @property
    def y(self):
        """a function that retrieves x
        """
        return self.__y

    @y.setter
    def y(self, y):
        """a function that sets the value of y
        Args:
            y: value of y
        """
        if not(isinstance(y, int)):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
            self.__y = y

    def area(self):
        """a function that returns the area value of the Rectangle instance
        """
        A = self.__width * self.__height
        return A

    def display(self):
        """ a function that prints in stdout the 
            Rectangle instance with the character # 
        """
        k = self.__width * '#'
        for i in range(self.__height):
            print(k)
        print()
