#!/usr/bin/python3
"""Define and implement function of object and class"""

def inherits_from(obj, a_class):
    """function that checks object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
