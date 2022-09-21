#!/usr/bin/python3

def pow(a, b):
    i = 1
    power = 1
    if b >= 0:
        while i <= b:
            power = power * a
            i = i + 1

    if b < 0:
        while i <= -1 * b:
            power = power * 1 / a
            i = i + 1
    return power
