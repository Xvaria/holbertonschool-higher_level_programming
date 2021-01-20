#!/usr/bin/python3
'Square'
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    'Square data'
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        'calculate area'
        return(self.__size * self.__size)

    def __str__(self):
        'square description'
        return("[Square] {}/{}".format(self.__size, self.__size))
