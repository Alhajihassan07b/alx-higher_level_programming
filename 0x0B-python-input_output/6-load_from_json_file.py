#!/usr/bin/python3

import json


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
