#!/usr/bin/python3

import sys
sum = 0
i = 1
if __name__ == "__main__":
    while i < len(sys.argv):
        sum = sum + int(sys.argv[i])
        i = i + 1
print(sum)
