#!/usr/bin/python3
""" Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization method"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """setter for x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter method for x"""

        return (self.__y)

    @y.setter
    def y(self, value):
        """setter for y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """public method area"""

        return self.__width * self.__height

    def display(self):
        """public method display"""

        print(self.__y * '\n', end="")
        for i in range(self.height):
            display = ""
            display += (self.__x * ' ')
            display += (self.width * '#')
            print(display)

    def __str__(self):
        """override str function"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """ update method for args"""

        attr = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])

        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns a dictionary of the attr"""

        attr = ['x', 'y', 'id', 'height', 'width']
        res = {}

        for key in attr:
            res[key] = getattr(self, key)
        return res
