#!/usr/bin/python3
""" Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class inheriting from base"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization method"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size calling self.width"""

        return self.width

    @size.setter
    def size(self, value):
        """setter for size using rectangle attr"""

        self.width = value
        self.height = value

    def __str__(self):
        """override str function"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.size}")

    def update(self, *args, **kwargs):
        """ update method for args"""

        if args is not None and len(args) != 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary with attributes"""
        attr = ['id', 'x', 'size', 'y']
        res = {}

        for key in attr:
            if key == 'size':
                res[key] = getattr(self, 'width')
            else:
                res[key] = getattr(self, key)
        return res
