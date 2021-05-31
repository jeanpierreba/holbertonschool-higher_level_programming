#!/usr/bin/python3

""" Module that contains a class Student """


class Student:
    """ Class that defines a student with first and last name and age """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):

            my_dic = self.__dict__.copy()
        else:
            my_dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return my_dic
