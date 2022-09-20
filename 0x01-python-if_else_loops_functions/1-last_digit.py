#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = abs(number) % 10
if k == 0:
    print(f'Last digit of {number} is {k} and is 0')
elif k < 6 and not 0 and number > 0:
    print(f'Last digit of {number} is {k} and is less than 6 and not 0')
elif k > 5 and number > 0:
    print(f'Last digit of {number} is {k} and is greater than 5')
elif number < 0:
    print(f'Last digit of {number} is {k * -1} and is less than 6 and not 0')
