#!/usr/bin/python3
"""
models module which contains the object's definitions
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class which has initializer methods of the Rectangle's object
    and inherits the base from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method doc"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area doc"""
        return self.__height * self.__width

    def display(self):
        """
        method which draws a figure
        """
        Stry = "\n" * self.__y
        print(Stry, end='')
        for i in range(self.__height):
            Strx = " " * self.__x
            print(Strx, end='')
            width = "#" * self.__width
            print(width)

    def __str__(self):
        """
        method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        attrs = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, attrs[i], args[i])

        for key in kwargs:
            setattr(self, key, kwargs[key])
