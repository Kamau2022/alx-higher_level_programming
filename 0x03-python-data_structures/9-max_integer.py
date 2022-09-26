#!/usr/bin/python3
def max_integer(my_list=[]):
    """the function finds the largest integer in a list
    Args:
       my_list: integers
    Returns:
        None or the largest integer
    """
    b = len(my_list)
    if b == 0:
        return None
    else:
        my_list.sort()
        k = my_list[-1]
        return k
