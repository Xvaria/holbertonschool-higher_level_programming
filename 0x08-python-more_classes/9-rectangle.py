#!/usr/bin/python3
'Rectangle'


class Rectangle:
    'class define a rectangle'
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        'starts our rectangle with default values'
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        'returns the area of the rectangle'
        a = self.__width * self.__height
        return(a)

    def perimeter(self):
        'returns the perimeter of the rectangle'
        if self.__width == 0 or self.height == 0:
            p = 0
        else:
            p = (self.__width * 2) + (self.__height * 2)
        return(p)

    def __str__(self):
        'returns a rectangle-shaped string according to its size'
        s = ""
        if self.__width == 0 or self.__height == 0:
            return(s)
        else:
            l = 1
            for i in range(self.__height):
                for j in range(self.__width):
                    s = s + str(self.print_symbol)
                if l < self.__height:
                    s = s + '\n'
                    l += 1
            return(s)

    def __repr__(self):
        'return a string representation of the rectangle'
        r = "Rectangle({}, {})".format(self.__width, self.__height)
        return(r)

    def __del__(self):
        'Print the message and instance of Rectangle is deleted'
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        'returns the biggest rectangle based on the area'
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        'returns a new Rectangle instance with width == height == size'
        return(cls(size, size))

    @property
    def width(self):
        'returns the width value of the rectangle'
        return(self.__width)

    @width.setter
    def width(self, value):
        'validates type of data and the size of the width of the rectangle'
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        'returns the height value of the rectangle'
        return(self.__height)

    @height.setter
    def height(self, value):
        'validates type of data and the size of the height of the rectangle'
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
