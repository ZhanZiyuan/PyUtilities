#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle
import sys
from pathlib import Path
from pprint import pprint
from typing import Any, Union


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


def convert_mpf_to_float(input_file_path: str,
                         read_key: Union[str, None] = None,
                         saved_file_path: Union[str, None] = None,
                         read_mode: str = "rb") -> Union[dict, list, None]:
    """
    Convert the `mpf` type to the `float` type.

    Args
    ----
    input_file_path: string
        The path of the input file.
    read_key: string or None
        The chosen read key. Default is `None`.
    saved_file_path: string or None
        The path of the output file. Default is `None`.
    read_mode: string
        The chosen read mode. Default is "rb".

    Returns
    -------
    If a file path is input, it will return `None`.
    Otherwise it will return a dictionary (no read key)
    or a list (there is a read key).
    """
    with open(input_file_path, read_mode, encoding=None) as file_object:
        file_contents: dict = pickle.load(file_object)

        if read_key is None:
            converted_file_contents = {}
            for key, value_list in file_contents.items():
                converted_value_list = []
                for sub_value_list in value_list:
                    converted_sub_value_list = [
                        sub_value_list[0],
                        [
                            float(mpf_number)
                            for mpf_number in sub_value_list[1]
                        ]
                    ]
                    converted_value_list.append(converted_sub_value_list)
                converted_file_contents.update({key: converted_value_list})

            if saved_file_path is None:
                return converted_file_contents
            elif saved_file_path is not None:
                print_to_file(
                    printable_object=converted_file_contents,
                    output_file_path=saved_file_path,
                    use_pprint=True,
                    write_mode="w+"
                )

        elif read_key is not None:
            read_value_list: list = file_contents[read_key]
            converted_value_list = []
            for sub_list in read_value_list:
                converted_sub_list = [
                    sub_list[0],
                    [
                        float(mpf_number)
                        for mpf_number in sub_list[1]
                    ]
                ]
                converted_value_list.append(converted_sub_list)

            if saved_file_path is None:
                return converted_value_list
            elif saved_file_path is not None:
                print_to_file(
                    printable_object=converted_value_list,
                    output_file_path=saved_file_path,
                    use_pprint=True,
                    write_mode="w+"
                )


def select_elements(input_file_path: str,
                    read_keys: Union[str, list],
                    selected_index: int,
                    saved_file_path: Union[str, None] = None,
                    read_mode: str = "rb") -> Union[dict, list, None]:
    """
    Convert the `mpf` type to the `float` type.

    Args
    ----
    input_file_path: string
        The path of the input file.
    read_keys: string or list
        The chosen read key(s).
    selected_index: int
        The index of the selected element in the sublist.
    saved_file_path: string or None
        The path of the output file. Default is `None`.
    read_mode: string
        The chosen read mode. Default is "rb".

    Returns
    -------
    If a file path is input, it will return `None`.
    Otherwise it will return a dictionary (a list of read keys)
    or a list (only one read key).
    """
    with open(input_file_path, read_mode, encoding=None) as file_object:
        file_contents: dict = pickle.load(file_object)

        if isinstance(read_keys, list):
            converted_selected_contents = {}
            for selected_key in read_keys:
                selected_value: list = file_contents[selected_key]
                converted_selected_value = []
                for sub_list in selected_value:
                    converted_sub_list = [
                        sub_list[0],
                        [float(sub_list[1][selected_index])]
                    ]
                    converted_selected_value.append(converted_sub_list)
                converted_selected_contents.update(
                    {selected_key: converted_selected_value}
                )

            if saved_file_path is None:
                return converted_selected_contents
            elif saved_file_path is not None:
                print_to_file(
                    printable_object=converted_selected_contents,
                    output_file_path=saved_file_path,
                    use_pprint=True,
                    write_mode="w+"
                )

        elif isinstance(read_keys, str):
            read_value_list: list = file_contents[read_keys]
            converted_value_list = []
            for sub_list in read_value_list:
                converted_sub_list = [
                    sub_list[0],
                    [float(sub_list[1][selected_index])]
                ]
                converted_value_list.append(converted_sub_list)

            if saved_file_path is None:
                return converted_value_list
            elif saved_file_path is not None:
                print_to_file(
                    printable_object=converted_value_list,
                    output_file_path=saved_file_path,
                    use_pprint=True,
                    write_mode="w+"
                )


if __name__ == "__main__":

    input_pickle_path = (
        "/home/zhanziyuan/python_assignments"
        "/catmap_test/ORR_thermo/ORR.pkl"
    )

    redirected_file_path = (
        "/home/zhanziyuan/python_assignments"
        "/catmap_test/ORR_thermo/redirected_output.log"
    )

    save_to_file_path = (
        "/home/zhanziyuan/python_assignments"
        "/catmap_test/ORR_thermo/mpf_to_float.log"
    )

    sample_dict = {
        "name": "Jane",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "hobby": "Reading"
    }

    print_to_file(
        sample_dict,
        redirected_file_path,
        True
    )

    convert_mpf_to_float(
        input_file_path=input_pickle_path,
        read_key="rate_map",
        saved_file_path=save_to_file_path,
        read_mode="rb"
    )

    select_elements(
        input_file_path=input_pickle_path,
        read_keys=[
            "forward_rate_constant_map",
            "reverse_rate_constant_map",
            "equilibrium_constant_map"
        ],
        selected_index=5,
        saved_file_path=save_to_file_path,
        read_mode="rb"
    )
