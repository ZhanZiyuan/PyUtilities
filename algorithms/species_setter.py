#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Please refer to:

1. https://segmentfault.com/a/1190000025164515
2. https://blog.csdn.net/qq_41035283/article/details/124551838
3. https://iphysresearch.github.io/blog/post/programing/python/property_setter/
"""

from __future__ import annotations

from typing import Union


class Species(object):
    """
    __doc__
    """
    def __init__(self, name: str) -> None:
        """
        __doc__
        """
        self.name = name
        self._mass = 0.0

    def __repr__(self) -> str:
        """
        __doc__
        """
        return str(
            {
                "name": self.name,
                "mass": self.mass
            }
        )

    @property
    def mass(self) -> Union[int, float]:
        """
        getter method
        """
        return self._mass

    @mass.setter
    def mass(self, mass_value: Union[int, float]) -> None:
        """
        setter method
        """
        if not isinstance(mass_value, (int, float)):
            raise TypeError("The value of mass must be a number.")
        if mass_value < 0:
            raise ValueError("The value of mass cannot be negative.")
        self._mass = mass_value

    def __add__(self, other: Species) -> Species:
        """
        add names
        """
        added_name = self.name + other.name
        return Species(added_name)


if __name__ == "__main__":

    Na = Species("Na")
    Cl = Species("Cl")

    NaCl = Na + Cl
    NaCl.mass = 58.4428

    print(NaCl)
    print(NaCl.name)
    print(NaCl.mass)
