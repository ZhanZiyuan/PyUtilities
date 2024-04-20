#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
from pathlib import Path
from typing import Union


def get_child_item_size(folder_path: str,
                        human_readable: bool = True) -> Union[dict, None]:
    """
    Get the size of each child item in the input directory
    in a human-readable format.
    """
    if Path(folder_path).is_dir():
        name_and_size = {}
        for child_item in Path(folder_path).iterdir():
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


if __name__ == "__main__":

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
            print(f"{size:>10}  {name}")
