#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Function that prints the first and last name given.

    Returns :
        Nothing

    Raises :
        TypeError in case the first name is not a string
        TypeError in case the last name is not a string
    """
    Full_name = print("My name is {} {}".format(first_name, last_name))
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == None:
        raise TypeError(
            "say_my_name() missing 1 required positional argument: {}".format(first_name))
    return Full_name	
