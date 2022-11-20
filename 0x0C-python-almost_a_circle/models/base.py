#!/usr/bin/python3
"""a base class"""
import json


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

    @classmethod
    def to_json_string(self, list_dictionaries):
        """a function that returns the JSON string
           representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
