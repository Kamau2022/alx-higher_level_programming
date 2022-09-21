#!/usr/bin/python3

for num in range(0, 100, 1):
    if num < 99:
        print("{:02d}" .format(num), end=", ")
    elif num == 99:
        print('99')
