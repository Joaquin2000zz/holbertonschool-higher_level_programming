#!/usr/bin/python3
"""module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class doc
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor doc
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter method
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        setter method
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        updater method
        """
        keys = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, keys[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
