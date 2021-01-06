#!/usr/bin/python3
'Square'


class Square:
    'class with one atribute, two errors, a public instance method and two\
    properties'
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        a = self.__size * self.__size
        return(a)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
