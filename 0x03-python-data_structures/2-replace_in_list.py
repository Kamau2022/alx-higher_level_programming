#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """ This function replaces an element of a list at a specific position
    Args:
        my_list: a list of integers
        idx: index 0f element to replace
        element: replaces an element at index idx
    Returns:
          original or the modified list
    """
    b = len(my_list) - 1
    if idx < 0 or idx > b:
        return my_list
    else:
        my_list[idx] = element
        return my_list
