#!/usr/bin/python3
'Square'


class Square:
    'class with one atribute, two errors, a public instance method and two\
    properties'
    def __init__(self, size=0, position=(0, 0)):
        'method to init'
        self.size = size
        self.position = position

    def area(self):
        'method to return area'
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        'method to print'
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        'property to return size'
        return(self.__size)

    @size.setter
    def size(self, value):
        'setter for new value to size'
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        'property to return position'
        return(self.__position)

    @position.setter
    def position(self, value):
        'setter for new value to position'
        e = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple or len(value) != 2 or type(value[0]) != int or
                value[0] < 0 or type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    continue
        self.__position = value
