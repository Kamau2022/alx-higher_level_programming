#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """a function that that prints x elements of a list.
    Args:
        my_list: list to print from
        x: number of elements
    Returns:
           real number of elements printed
    """
    a = my_list
    p = 0
    while p < x:
        try:
            print("{:d}" .format(a[p]), end='')
            p = p + 1
        except IndexError:
            break
    print()
    return p
