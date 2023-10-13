#!/usr/bin/python3
"""almost_a_circle"""


class Base:
    """
    A base class for object management.
    This class provides a mechanism for managing object identifiers.
    Attributes:
        __nb_objects (int): A private class variable.
    Methods:
        __init__: Initializes an object with a unique identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an object with a unique identifier.
        If an identifier is provided, it is assigned to the object.
        Args:
            id (int, optional): An identifier for the object.
        """

        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
