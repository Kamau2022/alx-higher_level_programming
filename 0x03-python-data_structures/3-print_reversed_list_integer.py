#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ this function prints integers in reverse
    Args:
        my_list: a list of integers
    Returns:
           nothing
    """
    b = len(my_list)
    i = -1
    if not my_list:
        return 
    while i >= -b:
        print("{:d}" .format(my_list[i]))
        i = i - 1
