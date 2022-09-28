#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function adds all unique integers in a list
    Args:
       my_list: a list of integers
    Returns:
           sum of the integers
    """
    sum = 0
    j = 0
    temp = []
    for i in my_list:
        if i not in temp:
            temp.append(i)
    my_list = temp
    b = len(my_list) - 1
    while j <= b:
        sum = sum + my_list[j]
        j = j + 1
    return sum
