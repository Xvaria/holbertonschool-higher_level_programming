#!/usr/bin/python3
'First Rectangle'
from models.base import Base


class Rectangle(Base):
    'inherits from Base'

    def __init__(self, width, height, x=0, y=0, id=None):
        'Private instance attributes'
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        'returns the area value of the Rectangle instance'
        return(self.__width * self.__height)

    def display(self):
        'prints in stdout the Rectangle instance with the character #'
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        'return rectangle properties'
        return('[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height))

    def to_dictionary(self):
        'returns the dictionary representation of a rectangle'
        return({'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y})

    def update(self, *args, **kwargs):
        'assigns an argument to each attribute'
        for i, j in kwargs.items():
            setattr(self, i, j)
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    @property
    def width(self):
        'return width'
        return(self.__width)

    @width.setter
    def width(self, value):
        'validate width'
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        'return height'
        return(self.__height)

    @height.setter
    def height(self, value):
        'validate height'
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        'return x'
        return(self.__x)

    @x.setter
    def x(self, value):
        'validate x'
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        'return y'
        return(self.__y)

    @y.setter
    def y(self, value):
        'validate y'
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
