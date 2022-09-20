#!/usr/bin/python3

for i in range(97, 123):
    b = chr(i)
    if b == 'e' or b == 'q':
        continue
    print("{}" .format(b), end="")
