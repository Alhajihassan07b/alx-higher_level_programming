#!/usr/bin/python3
"""Define of LokedClass"""


class LockedClass:
    """
    prevent the from isinstantiating new Lokedclass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
