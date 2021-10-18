#!/usr/bin/python3
"""
This module contains a class called Base
"""
import json



class Base:
    """Base class for upcoming classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of objects to a file"""
        if list_objs is None:
            list_dict = []
        else:
            list_dict = []
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        else:
            json_list = (json.loads(json_string))
            return json_list
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance by processing a dictionary"""
        li = []
        dummy = cls(1, 1)
        #dummy.update(**dictionary)
        return dummy
