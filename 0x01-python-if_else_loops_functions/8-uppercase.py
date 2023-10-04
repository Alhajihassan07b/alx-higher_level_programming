#!/usr/bin/python3
def to_uppercase(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

def uppercase(str):
    string_new = ""
    for char in str:
        string_new += "%c" % to_uppercase(char)
    print("{:s}".format(string_new))
