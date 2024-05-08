#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Union


@dataclass
class Element(object):
    """
    __doc__
    """
    name: str
    mass: Union[int, float] = 0.0


class Species(Element):
    """
    __doc__
    """

    @property
    def stoichiometry(self) -> list:
        """
        __doc__
        """
        return re.findall(r"\d+", self.name)

    def __add__(self, other: Species) -> Species:
        """
        add names
        """
        added_name = self.name + other.name
        added_mass = self.mass + other.mass
        return Species(added_name, added_mass)

    def __mul__(self, other: int) -> Species:
        """
        __doc__
        """
        multiplied_name = f"{self.name}{other}"
        multiplied_mass = other * self.mass
        return Species(multiplied_name, multiplied_mass)

    def __rmul__(self, other: int) -> Species:
        """
        __doc__
        """
        return self.__mul__(other)


if __name__ == "__main__":

    F = Species("F", 18.998)
    Na = Species("Na", 22.990)
    Cl = Species("Cl", 35.45)

    F2 = F * 2
    Cl2 = 2 * Cl
    NaCl = Na + Cl

    print(F2.name)
    print(F2.mass)
    print(F2.stoichiometry)

    print(Cl2.name)
    print(Cl2.mass)
    print(Cl2.stoichiometry)

    print(NaCl.name)
    print(NaCl.mass)
    print(NaCl.stoichiometry)
