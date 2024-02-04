#!/usr/bin/python3
class Square:
    """
    Square Class
    """
    def __init__(self, size=0):
        """
        Initializes the Square instance with a size.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2
