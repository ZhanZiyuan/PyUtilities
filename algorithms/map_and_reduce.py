#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Please refer to:
https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
"""

from functools import reduce
from typing import Union


def normalize_name(name: str) -> str:
    """
    Normalize the input English name.
    """
    # return name.lower().capitalize()
    return name.title()


def get_product_of_numbers(numbers: list) -> Union[int, float]:
    """
    Get the product of numbers in the input list.
    """
    return reduce(
        lambda x, y: x*y,
        numbers
    )


def sum_dict_values(input_dict: dict) -> Union[int, float]:
    """
    Sum the values of the input dictionary.
    """
    return reduce(
        lambda x, y: x + y,
        input_dict.values()
    )


def sum_dict_value_square(input_dict: dict) -> Union[int, float]:
    """
    Sum the squares of values of the input dictionary.
    """
    return reduce(
        lambda x, y: x + y**2,
        input_dict.values(),
        0
    )


def sum_dict_value_square_no_initial(input_dict: dict) -> Union[int, float]:
    """
    Sum the squares of values of the input dictionary.
    """
    return reduce(
        lambda x, y: x**2 + y**2,
        input_dict.values()
    )


def get_sum_of_square(input_dict: dict) -> Union[int, float]:
    """
    Sum the squares of values of the input dictionary.
    """
    return sum(
        [i**2 for i in input_dict.values()]
    )


if __name__ == "__main__":

    given_names = ['adam', 'LISA', 'barT']

    letters_and_numbers = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4
    }

    print(
        list(
            map(normalize_name, given_names)
        )
    )

    print(
        get_product_of_numbers(
            [1.0, 2.0, 3.0, 4.0]
        )
    )

    print(
        sum_dict_values(letters_and_numbers)
    )

    print(
        sum_dict_value_square(letters_and_numbers)
    )

    print(
        sum_dict_value_square_no_initial(letters_and_numbers)
    )

    print(
        get_sum_of_square(letters_and_numbers)
    )
