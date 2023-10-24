#!/usr/bin/python3

"""Define class Square"""
class Square:
    """Initialize a new square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The size of the new square.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size__ = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size__ * self.__size__)
