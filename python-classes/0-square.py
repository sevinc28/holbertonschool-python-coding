#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value verification needed).
        """
        self.__size = size  # Private attribute to store the size of the square

