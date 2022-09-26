#!/usr/bin/python3

def element_at(my_list, idx):
    """ a function that retrieves an element from a list
    Args:
        my_list: a list of integers
        idx: the element to be retrieved
    Returns:
        None or the retrieved element
    """
    b = len(my_list) - 1
    if idx < 0 or idx > b:
        return None
    else:
        return my_list[idx]
