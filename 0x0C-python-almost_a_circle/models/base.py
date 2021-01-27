#!/usr/bin/python3
'Base class'
import json


class Base():
    'This class will be the base of all other classes in this project'
    __nb_objects = 0

    def __init__(self, id=None):
        'manage id attribute in all your future classes and to avoid\
         duplicating the same code'
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        'returns the JSON string representation of list_dictionaries'
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return('[]')
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        'writes the JSON string representation of list_objs to a file'
        with open(cls.__name__ + '.json', mode='w') as w:
            if list_objs is None:
                w.write('[]')
            else:
                w.write(cls.to_json_string([item.to_dictionary()
                                            for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        'returns the list of the JSON string representation json_string'
        if json_string is None or len(json_string) == 0:
            return([])
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        'returns an instance with all attributes already set'
        if cls.__name__ == 'Rectangle':
            t = cls(1, 1)
        if cls.__name__ == 'Square':
            t = cls(1)
        t.update(**dictionary)
        return(t)

    @classmethod
    def load_from_file(cls):
        'returns a list of instances'
        f = []
        with open(cls.__name__ + '.json', mode='r') as r:
            t = r.read()
        t = cls.from_json_string(t)
        for i in t:
            if type(i) != dict:
                f.append(cls.create(**i))
            else:
                f.append(i)
        return(f)
