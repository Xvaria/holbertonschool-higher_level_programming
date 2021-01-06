#!/usr/bin/python3
'Square'


class Square:
    'class with one atribute, two errors, a public instance method and two\
    properties'
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        if self.size == 0:
            print()
        if self.position[1] > 0:
            for k in range(self.position[1]):
                print()
        for i in range(self.__size):
            for l in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or value[0] < 0 or
            value[1] < 0 or type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
