#!/usr/bin/python3

def is_lower(c):
    for char in c:
        if(ord(char) >= 97 and ord(char) <= 122):
            return True
        else:
            return False 