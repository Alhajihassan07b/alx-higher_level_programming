#!/usr/bin/python3

def read_file(filename=""):
    """print content of a UTF8 test file of stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
