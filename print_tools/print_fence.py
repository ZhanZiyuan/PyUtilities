#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
print_fence - print ASCII character fences

References:
1. [ASCII Art](https://blog.csdn.net/u014636245/article/details/83661559)
2. [art · PyPI](https://pypi.org/project/art/)
3. [pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)

TODO:
1. Print colored fences.
2. Process multiple rows of strings.
"""

import argparse
from pathlib import Path
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
    set_width: int
        The augment to the width of the fence.
        Default is `4`.
    set_height: int
        The augment to the height of the fence.
        Default is `5`.
    fence_style: str
        The style of the printed fence.
        Default is `"hyphen"`.
    add_blank_line: bool
        If `True`, a blank line will be inserted
        at the end of the printed contents.
        Default is `True`.
    sleep_time: int, float, or `None`
        The interval of each printing.
        Default is `None`.

    Returns
    -------
    Returns `None`: print the input contents.
    """
    colors = {
        "Black": "\033[30m",
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Yellow": "\033[33m",
        "Blue": "\033[34m",
        "Magenta": "\033[35m",
        "Cyan": "\033[36m",
        "White": "\033[37m",
        "Default": "\033[39m"
    }

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


def main() -> None:
    """
    The main function.
    """
    parser = argparse.ArgumentParser(
        prog=f"{Path(__file__).name}",
        description=(
            "Use ASCII characters to fence what you would like to print."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "contents",
        nargs="?",
        type=str,
        help="The printed contents."
    )
    parser.add_argument(
        "-p",
        "--printed-contents",
        type=str,
        help="The contents to be printed."
    )
    parser.add_argument(
        "-s",
        "--fence-style",
        default="hyphen",
        type=str,
        choices=["hyphen", "asterisk"],
        help=(
            "The style of the fence.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-b",
        "--blank-line",
        default="yes",
        type=str,
        choices=["yes", "no"],
        help=(
            "Whether to insert a blank line "
            "at the end of the printed contents or not.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-t",
        "--sleep-time",
        default="no",
        type=str,
        help=(
            "The interval of each printing.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-sw",
        "--set-width",
        default=4,
        type=int,
        help=(
            "The width of the fence.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-sh",
        "--set-height",
        default=5,
        type=int,
        help=(
            "The height of the fence.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version="%(prog)s 5.0.0"
    )

    command_args = parser.parse_args()

    if command_args.contents is not None:
        print_fence(
            contents=command_args.contents,
            set_width=command_args.set_width,
            set_height=command_args.set_height,
            fence_style=command_args.fence_style,
            add_blank_line=True if command_args.blank_line == "yes" else False,
            sleep_time=None if command_args.sleep_time == "no" else float(command_args.sleep_time)
        )
    elif command_args.contents is None:
        if command_args.printed_contents is not None:
            print_fence(
                contents=command_args.printed_contents,
                set_width=command_args.set_width,
                set_height=command_args.set_height,
                fence_style=command_args.fence_style,
                add_blank_line=True if command_args.blank_line == "yes" else False,
                sleep_time=None if command_args.sleep_time == "no" else float(command_args.sleep_time)
            )
        elif command_args.printed_contents is None:
            parser.print_usage()


if __name__ == "__main__":

    main()
