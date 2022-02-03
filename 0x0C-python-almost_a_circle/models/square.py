#!/usr/bin/python3
"""module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class doc"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor doc"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str doc"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"
