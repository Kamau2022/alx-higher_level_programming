#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = len(my_list)
    i = 0
    for i in my_list:
        while i <= b:
            if my_list[i] == 0 or my_list[i] % 2 == 0:
                i = i + 1
                return my_list[i], False
            elif my_list[i] % 2 != 0:
                return my_list[i], False
                continue
