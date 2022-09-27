#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ a print list function
    Args:
        my_list: a list of integers
    """
    b = my_list
    c = len(b) - 1
    i = 0
    while i <= c:
        print("{:d}" .format(b[i]))
        i = i + 1
