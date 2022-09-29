#!/usr/bin/python3
def best_score(a_dictionary):
    k = None
    """ function that finds key with biggest integer value
    Args:
      a_dictionary: include keys
    Returns:
          a key with the biggest integer value
    """
    if a_dictionary == k:
        return None
    elif a_dictionary == {}:
        return None
    else:
        k = max(a_dictionary, key=lambda k: a_dictionary[k])
        return k
