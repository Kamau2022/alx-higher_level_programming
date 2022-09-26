#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """function that deletes an item at a specific position
    Args:
       my_list: a list of items
       idx: position where an item is deleted
    Returns:
        my_list
    """
    b = len(my_list) - 1
    if idx < 0 or idx > b:
        return my_list
    else:
        del my_list[idx]
        return my_list
