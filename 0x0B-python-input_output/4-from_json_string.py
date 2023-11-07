#!/usr/bin/python3
"""Define string object"""

import json

def from_json_string(my_str):
    """ function that returns the JSON representation of an object"""
    return json.loads(my_str)
