#!/usr/bin/python3
"""Square class module"""

class Square:
    """A class that defines a square"""

    def __init__(self, size):
        """
        Constructor method to initialize the square with a given size.

        Args:
            size: The size of the square (no type/value check required here).
        """
        self.__size = size  # Private attribute to store the size of the square
