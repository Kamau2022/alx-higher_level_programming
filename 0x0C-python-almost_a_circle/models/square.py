#!/usr/bin/python3
"""a square that imports  attributes from a rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that describes attributes of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """a class constructor
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """a function that retrieves size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """a function that sets value of size
        """
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """a method that assigns attributes
        Args:
            *args: number of arguments
            **kwargs: a double pointer to a dictionary
        """
        a = ["id", "size", "x", "y"]
        for i in range(len(args)):
            for j in range(len(a)):
                if a[i] == a[j]:
                    setattr(self, a[i], args[i])
        i = 0
        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for i in range(len(a)):
                    if key == a[i]:
                        setattr(self, a[i], val)

    def __str__(self):
        """a function that returns [Square] (<id>) <x>/<y> - <size>
        """
        s = (f"[Square] ({self.id}) {self.x}/{self.y}"
             f" - {self.size}")
        return s

    def to_dictionary(self):
        """ a function that returns the dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.__size, 'y': self.y}
