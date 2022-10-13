#!/usr/bin/python3
"""a program that demonstrates use of getter and setter"""


class Square:
    """This class defines a square"""
    def __init__(self, __size=0):
        self.__size = __size

    def area(self):
        """a function that returns the current square area"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """a function to retrieve data"""
        return self.__size

    @size.setter
    def size(self, value):
        """a function that sets data"""
        if not(isinstance(value, (int))):
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        i = 0
        k = self.__size
        if k == 0:
            print()
        else:
            for i in range(k):
                for i in range(k):
                    print('#', end='')
                print()
