#!/usr/bin/python3
'the Square'
from models.rectangle import Rectangle


class Square(Rectangle):
    'inherits from Rectangle'

    def __init__(self, size, x=0, y=0, id=None):
        'Private instance attributes'
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        'return square properties'
        return('[{}] ({}) {}/{} - {}'.format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.__size))

    def update(self, *args, **kwargs):
        'assigns attributes'
        for i, j in kwargs.items():
            setattr(self, i, j)
        try:
            self.id = args[0]
            self.__size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        'returns the dictionary representation of a Square'
        return({'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y})

    @property
    def size(self):
        'return the rectangle size'
        return(self.__size)

    @size.setter
    def size(self, value):
        'assign the same value to width and the height'
        self.__size = value
