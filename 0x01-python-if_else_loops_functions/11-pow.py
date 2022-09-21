#!/usr/bin/python3

def pow(a, b):
    i = 1
    power = 1
    j = 1
    num = -1 * b
    k = 1 / a
    if b >= 0:
        while i <= b:
            power = power * a
            i = i + 1

    if b < 0:
        while j <= num:
            power = power * k
            j = j + 1
    return power
