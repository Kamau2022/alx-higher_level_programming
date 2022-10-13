#!/usr/bin/python3
"""a program that validate that size is correct before initializing it"""


class Square:
    """This class defines a square"""
    def __init__(self, __size=0):
        if not(isinstance(__size, (int))):
            raise TypeError("size must be an integer")
        self.__size = __size
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        """a function that returns the current square area"""
        return(self.__size * self.__size)
