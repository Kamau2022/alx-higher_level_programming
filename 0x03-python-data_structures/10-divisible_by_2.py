#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = len(my_list) - 1
    i = 0
    while i <= b:
        if my_list[i] % 2 == 0:
            return my_list[i]
        else:
            return False
    i = i + 1
