#!/usr/bin/python3
def multiple_returns(sentence):
    b = len(sentence)
    if b == 0:
        return b, None
    else:
        k = sentence[0]
        return b, k
