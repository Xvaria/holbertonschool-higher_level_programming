#!/usr/bin/python3lbertonschool-higher_level_programming/0x0A-python-inheritance$ cat 8-rectangle.py
'Rectangle inherits from BaseGeometry'
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    'class Rectangle'
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        'calculates area'
        return(self.__width * self.__height)

    def __str__(self):
        'rectangle description'
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
