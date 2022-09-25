#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == '__main__':

    b = dir(hidden)

for name in b:
    if name[0:2] != '__':
        print(name)
