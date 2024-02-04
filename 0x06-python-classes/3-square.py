#!/usr/bin/python3
"""
Square Module
"""


class Square:
    """
    Square Class
    """
    def __init__(self, size=0):
        """
        Initializes the Square instance with a size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2
