#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
print_fence - print ASCII character fences

version 3.0

Modified manually on 2023-05-18 10:25

References:
1. [ASCII Art](https://blog.csdn.net/u014636245/article/details/83661559)
2. [art · PyPI](https://pypi.org/project/art/)
3. [pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)
"""

from time import sleep
from typing import Any, Union


def print_fence(content: Any,
                fence_style: str = "hyphen",
                end_line: bool = True,
                sleep_time: Union[int, float] = 0.1) -> None:
    """ 
    Use ASCII characters to fence what you would like to print. 

    Args
    ----
    content: Any
        The contents you want to print.
    fence_style: string
        The style of the printed fence.
        Default is "hyphen".
    end_line: bool
        If `True`, a blank line will be inserted
        at the end of the print contents.
    sleep_time: integer or float
        The set printing interval.
        Default is 0.1 seconds.

    Returns
    -------
    Returns `None`: print the input contents.

    NOTE: This function can only process one line of string by now.
    """

    # define the width and height of the fence
    content = str(content)  # NOTE: `str()` is added here.
    width = len(content) + 4
    height = 5

    # output ASCII character fences
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
            padding_left = ' ' * ((width - len(content)) // - 1)  # NOTE: the original form: ((width - len(content)) // 2 - 1)
            padding_right = ' ' * ((width - len(content)) // 2 - 1 + (width - len(content)) % 2)
            if fence_style == "hyphen":
                print(f'| {padding_left}{content}{padding_right}|\n', end='')
            elif fence_style == "asterisk":
                print(f'* {padding_left}{content}{padding_right}*\n', end='')
            else:
                raise ValueError(f'Invalid fence style: "{fence_style}"')
            sleep(sleep_time)
        else:
            print(fence_side, end='')
            sleep(sleep_time)
    if fence_style == "hyphen":
        print(fence_top[:-2] + '+', end='')
    elif fence_style == "asterisk":
        print(fence_top[:-2] + '*', end='')
    else:
        raise ValueError(f'Invalid fence style: "{fence_style}"')

    if end_line:
        # This part is newly added on 2023-05-19 22:37.
        # To insert a blank line at the end of the print contents.
        # Default is `True`.
        print('\n')
    elif not end_line:
        pass


if __name__ == "__main__":

    # test the function `print_fence()` and output different ASCII fences

    print_fence("Hello world!")
    print_fence("Python is awesome.", end_line=False)
    print_fence("Python is awesome.", end_line=True)

    print_fence([10, 20, 30, 40])

    try:
        import numpy as np

        print_fence(np.array([10, 20, 30, 40]), fence_style="asterisk")
    except ImportError:
        pass

    try:
        import sympy as sm

        y, x1, x2, x3 = sm.symbols("y, x1, x2, x3")
        func = x1**2 + x2**2 + x3**2
        print_fence(func, fence_style="asterisk")
    except ImportError:
        pass
