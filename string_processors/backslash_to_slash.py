#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pathlib import Path


def convert_to_raw_string(original_string: str) -> str:
    """
    Convert the input string to a raw string.
    """
    return rf"{original_string}"


def backslash_to_slash_path(original_path: str) -> str:
    """
    Replace backslashes in the input path
    on a Windows system with slashes.
    """
    return Path(rf"{original_path}").as_posix()


def backslash_to_slash_str(path: str) -> str:
    """
    convert backslashes to slashes
    """
    return path.replace("\\", "/")


def split_long_str(long_str: str,
                   length_of_fragment: int) -> str:
    """
    Split a long string into fragments.
    """
    return "\n".join(
        [
            long_str[index: index+length_of_fragment]
            for index in range(0, len(long_str), length_of_fragment)
        ]
    )


if __name__ == "__main__":

    windows_path_c_01 = (
        r"C:\Users\user\Downloads\test_merge_10.py"
    )

    windows_path_d_01 = (
        r"D:\zigzag\Python Assignments\temporary"
        r"\kinopt_0.6_local\src\qssa\objective_func_merge_10.py"
    )

    print(
        convert_to_raw_string(windows_path_c_01),
        "\n",
        type(convert_to_raw_string(windows_path_c_01))
    )

    print(
        convert_to_raw_string(windows_path_d_01),
        "\n",
        type(convert_to_raw_string(windows_path_d_01))
    )

    print(
        backslash_to_slash_path(windows_path_c_01),
        "\n",
        type(backslash_to_slash_path(windows_path_c_01))
    )

    print(
        backslash_to_slash_path(windows_path_d_01),
        "\n",
        type(backslash_to_slash_path(windows_path_d_01))
    )
