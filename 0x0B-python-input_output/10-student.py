#!/usr/bin/python3
'Student to JSON'


class Student():
    'defines a student'
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        'retrieves a dictionary representation of a Student instance'
        if type(attrs) != list:
            return(self.__dict__)
        t = {}
        for i in attrs:
            if type(i) != str:
                return(self.__dict__)
            if i in self.__dict__.keys():
                t[i] = self.__dict__[i]
        return(t)
