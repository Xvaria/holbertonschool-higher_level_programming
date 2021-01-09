#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) == int or type(a) == float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) == int or type(b) == float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    c = a + b
    return(c)
