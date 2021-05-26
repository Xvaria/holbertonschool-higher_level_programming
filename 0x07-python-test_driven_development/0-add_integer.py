#!/usr/bin/python3
'add integers'


def add_integer(a, b=98):
    ''' Function to add two integers or floats '''

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

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
