#!/usr/bin/python
def multiply_list_map(my_list=[], number=0):
    """function multiplies a list with a number
    Args:
      my_list: values
      number: number multiplied by values in my_list
    Returns:
         a list with all values multiplied by a number
    """
    return list(map(lambda x: x * number, my_list))
