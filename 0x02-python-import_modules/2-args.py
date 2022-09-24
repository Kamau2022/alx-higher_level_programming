#!/usr/bin/python3

import sys
if __name__ == "__main__":
    i = 1
if len(sys.argv) - 1 == 1:
    print(len(sys.argv) - 1, "argument:")

elif len(sys.argv) - 1 == 0:
    print(len(sys.argv) - 1, "arguments.")

elif len(sys.argv) - 1 > 1:
    print(len(sys.argv) - 1, "arguments:")

while i <= len(sys.argv) - 1:
    print(f"{i}:", sys.argv[i])
    i = i + 1
