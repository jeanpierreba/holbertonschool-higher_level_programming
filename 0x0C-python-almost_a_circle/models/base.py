#!/usr/bin/python3

""" Module that contains a class Base for other modules """

import json
import os


class Base:
    """ Class that defines the Base model """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            js_str = "[]"
        else:
            js_str = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, 'w') as my_file:
            my_file.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_t = []
        dict_list = []
        if os.path.exists(filename):
            with open(filename) as my_file:
                read = my_file.read()
                dict_list = cls.from_json_string(read)
                for i in dict_list:
                    list_t.append(cls.create(**i))
        return list_t
