#!/usr/bin/python3

"""Define square"""

class Square:
    """Represent square"""


    def __init__(self, size=0):
        """Initialize square"""
        self.size = size


    @property
    def size(self):
        """To retrieve it."""
        return self.__size__

    @size.setter
    def size(self, value):
        """Initialze new square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = value


    def area(self):
        """return current square area"""
        return self.__size__ ** 2

    def my_print(self):
        """Print stdout the square with character #"""
        if self.__size__ == 0:
            print()
        else:
            for i in range(self.__size__):
                print("#" * self.__size__)
