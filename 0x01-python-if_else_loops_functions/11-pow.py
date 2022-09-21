#!/usr/bin/python3

def pow(a, b):
    i = 1
    power = 1
    j = 1
    if b >= 0:
        while i <= b:
            power = power * a
            i = i + 1

    if b < 0:
        while j <= -1 * b:
            power = power * a
            j = j + 1
        power = 1 / power
    return power
