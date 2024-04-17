#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
from pathlib import Path
from typing import Union


def get_file_size(file_path: str,
                  human_readable: bool = True) -> str:
    """
    Return the size of the file
    at the given path in a human-readable format.
    """
    file_size = Path(file_path).stat().st_size

    if human_readable:
        return format_size(file_size)
    else:
        return str(file_size)


def format_size(size: Union[int, float]) -> str:
    """
    Convert the given size in bytes
    to a human-readable format.

    The maximum unit is "PB".
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog=f"{Path(__file__).name}",
        description="Calculate the size of the specified file.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-p",
        "--file_path",
        default=__file__,
        type=str,
        help=(
            "The path to the file.\n"
            "The default is the path to the script itself: %(default)s"
        )
    )
    parser.add_argument(
        "-r",
        "--human_readable",
        default="yes",
        type=str,
        choices=["yes", "no"],
        help=(
            "Print the size in human readable format (e.g., 1K 234M 2G).\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version="%(prog)s 1.0.0"
    )

    command_args = parser.parse_args()

    size_of_specified_file = get_file_size(
        file_path=command_args.file_path,
        human_readable=True if command_args.human_readable == "yes" else False
    )

    print(
        f'The size of the file "{Path(command_args.file_path).name}" '
        f'is {size_of_specified_file}.'
    )
