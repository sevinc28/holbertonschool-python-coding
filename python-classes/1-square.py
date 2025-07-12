#!/usr/bin/python3
"""Kvadrat adli sinif yaradiriq"""

class Square:
    """Olcusune gore kvadrat teyin edirik"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("olcu tam eded olmalidir")
        if size < 0:
            raise ValueError("olcu 0 ve ya 0-dan boyuk olmalidir")
        self,__size = size
