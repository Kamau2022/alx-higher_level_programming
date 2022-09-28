#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function returns a set of all elements present in only one set
    Args:
      set_1: the first set
      set_2: the second set
    Returns:
          a set of all elements present in only one set.
    """
    k = set_1.symmetric_difference(set_2)
    return k
