#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
https://blog.csdn.net/zhangyixin_618/article/details/89526717

https://www.cnblogs.com/unclemac/p/12783387.html
"""

import argparse
import re
from pathlib import Path
from typing import Union

COLORS = {
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


def get_child_item_size(folder_path: str,
                        human_readable: bool = True) -> Union[dict, None]:
    """
    Get the size of each child item in the input directory
    in a human-readable format.
    """
    if Path(folder_path).is_dir():
        name_and_size = {}
        for child_item in sorted(Path(folder_path).iterdir(), key=lambda x: re.sub('[^A-Za-z0-9]+', '', x.name)):
            file_name = Path(child_item).name
            file_size = Path(child_item).stat().st_size
            if human_readable:
                name_and_size.update(
                    {file_name: format_size(file_size)}
                )
            else:
                name_and_size.update(
                    {file_name: str(file_size)}
                )
        return name_and_size
    elif not Path(folder_path).is_dir():
        raise ValueError(
            "The input path is not a directory."
        )
    return None


def format_size(file_size: Union[int, float]) -> str:
    """
    Convert the given size in bytes
    to a human-readable format.

    The maximum unit is "PB".
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if file_size < 1024:
            return f"{file_size:.2f} {unit}"
        file_size /= 1024
    return f"{file_size:.2f} PB"


def main() -> None:
    """
    __doc__
    """
    parser = argparse.ArgumentParser(
        prog=f"{Path(__file__).name}",
        description=(
            "Calculate the size of each child item "
            "in the specified directory."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "path",
        nargs="?",
        type=str,
        help="The specified directory."
    )
    parser.add_argument(
        "-p",
        "--folder_path",
        default=Path(__file__).parent,
        type=str,
        help=(
            "The specified directory.\n"
            "The default is the logical parent of the script itself: %(default)s"
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
        "-c",
        "--color",
        default="Default",
        type=str,
        # choices=list(COLORS.keys()),
        help=(
            "Specify the color of the printed files or directories.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version="%(prog)s 1.0.4"
    )

    command_args = parser.parse_args()

    path_passed = command_args.path if command_args.path is not None else command_args.folder_path
    size_of_child_item = get_child_item_size(
        folder_path=path_passed,
        human_readable=True if command_args.human_readable == "yes" else False
    )

    print("\n")
    print(
        f"Directory: {Path(path_passed).absolute()}"
    )
    print("\n")

    if size_of_child_item is not None:
        print("Length  Name".rjust(16))
        print("------  ----".rjust(16))
        for name, size in size_of_child_item.items():
            color = COLORS[command_args.color.capitalize()]
            print(f"{color}{size:>10}  {name}{COLORS['Default']}")
        print("\n")


if __name__ == "__main__":

    main()
