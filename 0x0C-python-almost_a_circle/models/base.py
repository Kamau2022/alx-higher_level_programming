#!/usr/bin/python3
"""a base class"""


class Base:
    """This class will be the “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
