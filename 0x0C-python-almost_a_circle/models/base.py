#!/usr/bin/python3

class Base:
    """
    A base class for object management.

    This class provides a mechanism for managing object identifiers.

    Attributes:
        __nb_objects (int): A private class variable representing the number of created objects.

    Methods:
        __init__: Initializes an object with a unique identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an object with a unique identifier.

        If an identifier is provided, it is assigned to the object. Otherwise, a unique identifier is generated and assigned.

        Args:
            id (int, optional): An identifier for the object. Defaults to None.
        """
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

