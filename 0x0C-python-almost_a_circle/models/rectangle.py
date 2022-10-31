#!/usr/bin/python3
"""a module showcasing attributes of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """a class that describes attributes of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """a function that retrieves width
        """
        return self.__width

    @width.setter
    def width(self, x):
        """a function that sets the value of width
        Args:
             x: value of width
        """
        self.__width = x

    @property
    def height(self):
        """a function that retrieves height
        """
        return self.__height

    @height.setter
    def height(self, y):
        """a function that sets value of height
        Args:
            y: value of height
        """
        self.__height = y
