#!/usr/bin/python3
"""a module showcasing attributes of a rectangle"""
from models.base import Base


class Rectangle(Base):
    """a class that describes attributes of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """a class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        k = ''
        for i in range(self.y):
            print(k)
        for i in range(self.height):
            for i in range(self.x):
                print(f'{k:1}', end='')
            for i in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """a function that returns [Rectangle]
           (<id>) <x>/<y> - <width>/<height>
        """
        k = (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
             f" - {self.width}/{self.height}")
        return k

    def update(self, *args, **kwargs):
        """a function to update the class
        Args:
            *args: number of arguments
            **kwargs: a double pointer to a dictionary
        """
        a = ["id", "width", "height", "x", "y"]
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

    def to_dictionary(self):
        """a function that returns the dictionary representation of a Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
