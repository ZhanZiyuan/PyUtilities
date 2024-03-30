#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
References:
1. [Method of outputting print content to a file](https://codeantenna.com/a/sVn1MvGp32)
2. [How to redirect printed output to a TXT file](https://cloud.tencent.com/developer/ask/sof/133755)
3. [Python file I/O](https://www.runoob.com/python/python-files-io.html)
4. [python check whether a file exists](https://www.runoob.com/w3cnote/python-check-whether-a-file-exists.html)
5. [Python try except else](http://c.biancheng.net/view/2315.html)
"""

import sys
from pathlib import Path
from pprint import pprint
from typing import Any


def print_to_file(printable_object: Any,
                  output_file_path: str = "print_to_file.log",
                  use_pprint: bool = False,
                  write_mode: str = "w+") -> None:
    """
    Redirect standard output to a `.txt` / `.log` file.

    Args
    ----
    printable_object: Any
        What you would like to print.
    output_file_path: string
        The path of the output file.
    use_pprint: bool
        Use `pprint` or not. Default is `False`.
    write_mode: string
        The chosen write mode. Default is "w+".

    Returns
    -------
    Returns `None`: print `printable_object`.
    """
    with open(output_file_path, write_mode, encoding="utf-8") as file_object:
        sys.stdout = file_object  # Perform operations that will write to file.
        if not use_pprint:
            print(printable_object)
        elif use_pprint:
            pprint(printable_object)
    sys.stdout = sys.__stdout__  # Restore standard output.
    try:
        from print_fence import print_fence
        print_fence(
            'Redirected the output to the file '
            f'"{Path(output_file_path).name}". '
        )
    except ImportError:
        print(
            'Redirected the output to the file '
            f'"{Path(output_file_path).name}". '
        )


if __name__ == "__main__":

    file_path_windows = (
        "C:/Users/user/Downloads"
        "/print_to_file.log"
    )

    file_path_linux = (
        "/home/zhanziyuan/python_assignments/yaml"
        "/print_to_file.log"
    )

    sample_dict = {
        "name": "Jane",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "hobby": "Reading"
    }

    try:
        print_to_file(
            sample_dict,
            file_path_windows,
            True
        )
    except FileNotFoundError:
        print_to_file(
            sample_dict,
            file_path_linux,
            True
        )
