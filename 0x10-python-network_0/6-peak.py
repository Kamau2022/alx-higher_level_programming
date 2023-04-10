#!/usr/bin/python3
"""a module to find the peak element"""


def find_peak(list_of_integers):
    """a function to find the peak element"""
    length = len(list_of_integers)
    start = 0
    end = l - 1
    if length == 0:
        return None
    while start < end:
        mid = int(start + (end - start) / 2)
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
