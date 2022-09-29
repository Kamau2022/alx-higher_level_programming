#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element
       by another in a new list
    Args:
        my_list: is the initial list
        search: is the element to replace in the list
        replace: is the new element
    Returns:
           new_element
    """
    new_list = my_list.copy()
    i = 0
    b = len(new_list)
    for i in range(0, b):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
