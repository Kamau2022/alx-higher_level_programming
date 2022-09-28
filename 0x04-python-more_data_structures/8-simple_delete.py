#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        k = i.pop("key", None)
        if k == None:
            return a_dictionary
        else:
            return a_dictionary
        
