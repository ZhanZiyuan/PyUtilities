#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
print_fence - print ASCII character fences

version 4.0

Modified manually on 2024-01-20 16:21

References:
1. [ASCII Art](https://blog.csdn.net/u014636245/article/details/83661559)
2. [art · PyPI](https://pypi.org/project/art/)
3. [pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)
"""

from time import sleep
from typing import Any, Union


def print_fence(contents: Any,
                set_width: int = 4,
                set_height: int = 5,
                fence_style: str = "hyphen",
                add_blank_line: bool = True,
                sleep_time: Union[int, float, None] = None) -> None:
    """
    Use ASCII characters to fence what you would like to print.

    Args
    ----
    contents: Any
        The contents you want to print.
    set_width: integer
        The augment to the width of the fence.
        Default is 4.
    set_height: integer
        The augment to the height of the fence.
        Default is 5.
    fence_style: string
        The style of the printed fence.
        Default is "hyphen".
    add_blank_line: bool
        If `True`, a blank line will be inserted
        at the end of the print contents.
        Default is `True`.
    sleep_time: integer, float, or `None`
        The set printing interval.
        Default is `None`.

    Returns
    -------
    Returns `None`: print the input contents.

    NOTE: This function can only process one line of string by now.
    """

    def pause(interval: Union[int, float, None]) -> None:
        """
        Pause printing.
        """
        if interval is None:
            pass
        elif isinstance(interval, (int, float)):
            sleep(interval)
        else:
            raise TypeError(
                f"Invalid type of `sleep_time`: {type(interval)}"
            )

    # Define the width and height of the fence
    #
    # NOTE: Convert `contents` of `Any` type to string type.
    contents = str(contents)
    width = len(contents) + set_width
    height = set_height

    # Output ASCII character fences
    if fence_style == "hyphen":
        fence_top = '+' + '-' * (width - 2) + '+\n'
        fence_side = '|' + ' ' * (width - 2) + '|\n'
    elif fence_style == "asterisk":
        fence_top = '*' + '*' * (width - 2) + '*\n'
        fence_side = '*' + ' ' * (width - 2) + '*\n'
    else:
        raise ValueError(f'Invalid fence style: "{fence_style}"')

    print(fence_top, end='')
    for i in range(height - 2):
        if i == (height - 2) // 2:
            padding_left = ' ' * ((width - len(contents)) // - 1)  # NOTE: The original form: ((width - len(content)) // 2 - 1)
            padding_right = ' ' * ((width - len(contents)) // 2 - 1 + (width - len(contents)) % 2)
            if fence_style == "hyphen":
                print(f'| {padding_left}{contents}{padding_right}|\n', end='')
            elif fence_style == "asterisk":
                print(f'* {padding_left}{contents}{padding_right}*\n', end='')
            else:
                raise ValueError(f'Invalid fence style: "{fence_style}"')
            pause(sleep_time)
        else:
            print(fence_side, end='')
            pause(sleep_time)
    if fence_style == "hyphen":
        print(fence_top[:-2] + '+', end='')
    elif fence_style == "asterisk":
        print(fence_top[:-2] + '*', end='')
    else:
        raise ValueError(f'Invalid fence style: "{fence_style}"')

    if add_blank_line:
        print("\n")
    elif not add_blank_line:
        pass


if __name__ == "__main__":

    print_fence(
        "Python is awesome.",
        add_blank_line=False
    )

    print_fence(
        "Python is awesome.",
        add_blank_line=True,
        sleep_time=1.0
    )

    import numpy as np
    import sympy as sm

    print_fence(
        np.array([10, 20, 30, 40]),
        fence_style="asterisk"
    )

    x1, x2, x3 = sm.symbols("x1 x2 x3")
    symbolic_func = x1**2 + x2**2 + x3**2

    print_fence(
        symbolic_func,
        fence_style="asterisk"
    )
