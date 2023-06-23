#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) > 2):
        tuple_a = (tuple_a[0], tuple_a[1])
    if (len(tuple_b) > 2):
        tuple_b = (tuple_b[0], tuple_b[1])
    if (len(tuple_a) == 2 and len(tuple_b) == 2):
        result = tuple([tuple_a[i] + tuple_b[i] for i in range(len(tuple_a))])
        return result
    if (len(tuple_b) == 0) and len(tuple_a) != 0:
        return tuple_a
    if (len(tuple_a) == 0) and len(tuple_b) != 0:
        return tuple_b
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (len(tuple_a), len(tuple_a))
    if (len(tuple_b) < 2) and len(tuple_a) == 2:
        s = (0,)
        tuple_s = tuple_b + s
        result = tuple([tuple_s[i] + tuple_a[i] for i in range(len(tuple_a))])
        return result
    if (len(tuple_a) < 2) and len(tuple_b) == 2:
        s = (0,)
        tuple_s = tuple_a + s
        result = tuple([tuple_s[i] + tuple_b[i] for i in range(len(tuple_b))])
        return result
    if (len(tuple_a) < 2) and len(tuple_b) < 2:
        s = (0,)
        tuple_a = tuple_a + s
        tuple_b = tuple_b + s
        result = tuple([tuple_a[i] + tuple_b[i] for i in range(len(tuple_b))])
        return result
