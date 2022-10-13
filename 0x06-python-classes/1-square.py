#!/usr/bin/python3
"""a program that demonstrates a  private instance attribute"""


class Square:
    """This class defines a square"""
    def __init__(self, __size="0"):
        self.__size = __size
