#!/usr/bin/python3


def print_last_digit(number):
    """function that prints the last digit of a number.
    """
    if number <= 0 or number > 0:
        k = abs(number) % 10
        print(k, end="")
    return abs(number) % 10
