#!/usr/bin/python3
from models.base import Base
"""almost_a_circle"""


class Rectangle(Base):
    """
    A class representing a rectangle.
    This class inherits from the Base class.
    Attributes:
        None
    Methods:
        __init__: Initializes a Rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): An identifier for the rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
	    """method"""
	    return (self.__width * self.__height)

    def display(self):
        """display method"""
        if self.__y > 0:
            print("{}".format((self.__y - 1) * '\n'))
        if self.__y == 0:
            pass
        for row in range(self.__height):
            print("{}{}".format(self.__x * ' ', self.__width * '#'))

    def __str__(self):
        """__str__ method"""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        rec = self.__class__.__name__
        i = self.id
        string = "[{}] ({}) {}/{} - {}/{}".format(rec, i, x, y, w, h)
        return string

    def update(self, *args):
        """update_method"""    
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, val in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, val)
