#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
An implementation of
`ls -lh` (GNU Coreutils) and `Get-ChildItem` (PowerShell)
in Python.

References:

1. https://blog.csdn.net/zhangyixin_618/article/details/89526717
2. https://www.cnblogs.com/unclemac/p/12783387.html
"""

import argparse
import re
from pathlib import Path
from typing import Union


def get_child_item(folder_path: str,
                   human_readable: bool = True) -> Union[dict, None]:
    """
    Get the size of each child item in the input directory
    in a human-readable format.
    """
    if Path(folder_path).is_dir():
        name_and_size = {}
        for child_item in sorted(Path(folder_path).iterdir(), key=set_order_of_items):
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


def set_order_of_items(item: Path) -> tuple:
    """
    Set the order of sorting.

    Parameters
    ----------
    item: Path
        The path to the file or directory.

    Returns
    -------
    tuple:
        A tuple containing the file status (file or directory),
        lower case file name,
        and the file name with alphanumeric characters removed.
    """
    return (
        item.is_file(),
        item.name.lower(),
        re.sub("[A-Za-z0-9]+", "", item.name)
    )


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
    The main function.
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
        "--folder-path",
        default=Path(__file__).parent,
        type=str,
        help=(
            "The specified directory.\n"
            "The default is the logical parent of the script itself: %(default)s"
        )
    )
    parser.add_argument(
        "-r",
        "--human-readable",
        default="yes",
        type=str,
        choices=["yes", "no"],
        help=(
            "Print the size in human readable format (e.g., 1K 234M 2G).\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-cd",
        "--color-dir",
        default="blue",
        type=str,
        choices=[k.lower() for k in colors],
        help=(
            "Specify the color of the printed subdirectories.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-cf",
        "--color-file",
        default="default",
        type=str,
        choices=[k.lower() for k in colors],
        help=(
            "Specify the color of the printed files.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-cp",
        "--color-path",
        default="green",
        type=str,
        choices=[k.lower() for k in colors],
        help=(
            "Specify the color of the absolute version of this path.\n"
            "The default is: %(default)s"
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version="%(prog)s 2.0.2"
    )

    command_args = parser.parse_args()

    path_passed = command_args.path if command_args.path is not None else command_args.folder_path
    child_item_and_size = get_child_item(
        folder_path=path_passed,
        human_readable=True if command_args.human_readable == "yes" else False
    )

    print("")
    print(
        "Directory: "
        f"{colors[command_args.color_path.capitalize()]}{Path(path_passed).absolute()}{colors['Default']}"
    )
    print("")

    if child_item_and_size is not None:
        print("Length  Name".rjust(16))
        print("------  ----".rjust(16))
        for name, size in child_item_and_size.items():
            if Path(path_passed).joinpath(name).is_dir():
                print(
                    f"{size:>10} {colors[command_args.color_dir.capitalize()]}{name}{colors['Default']}"
                )
            elif Path(path_passed).joinpath(name).is_file():
                print(
                    f"{size:>10} {colors[command_args.color_file.capitalize()]}{name}{colors['Default']}"
                )


if __name__ == "__main__":

    main()
