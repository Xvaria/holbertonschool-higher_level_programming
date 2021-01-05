#!/usr/bin/python3
'Square'


class Square:
    'class with one atribute, two errors and a public instance method'
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        a = self.__size * self.__size
        return(a)
