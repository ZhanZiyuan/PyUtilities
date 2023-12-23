#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pathlib import Path

import pandas as pd


def extract_lines_from_txt(input_file: str,
                           interval: int,
                           output_file: str,
                           use_header: bool = True) -> None:
    """
    Extract one line every N lines from a plain text file.
    """
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            line_number = 0
            if use_header:
                header = f_in.readline()
                f_out.write(header)
            while True:
                line = f_in.readline()
                if not line:
                    break
                line_number += 1
                if (
                    (use_header and line_number % interval == 0)
                    or (not use_header and (line_number - 1) % interval == 0)
                ):
                    f_out.write(line)
    print(
        'Extraction of lines from the file: '
        f'"{Path(input_file).name}" completed. '
    )


def extract_lines_from_csv(input_file: str,
                           interval: int,
                           output_file: str,
                           use_header: bool = False) -> None:
    """
    Extract one line every N lines from a `.csv` file.
    """
    if not use_header:
        df = pd.read_csv(input_file, header=None)
        extracted_df = df.iloc[::interval, :]
        extracted_df.to_csv(output_file, header=False, index=False)
    elif use_header:
        df = pd.read_csv(input_file)
        extracted_df = df.iloc[::interval, :]
        extracted_df.to_csv(output_file, index=False)
    print(
        'Extraction of lines from the file: '
        f'"{Path(input_file).name}" completed. '
    )


def txt_to_csv(input_file: str,
               output_file: str,
               use_header: bool = True) -> None:
    """
    Convert a plain text file to a `.csv` file.
    """
    if use_header:
        df = pd.read_csv(input_file, delimiter=r'\s+')
        df.to_csv(output_file, index=False)
    elif not use_header:
        df = pd.read_csv(input_file, delimiter=r'\s+', header=None)
        df.to_csv(output_file, header=False, index=False)
    print(
        f'Conversion from the file "{Path(input_file).name}" '
        f'to the file "{Path(output_file).name}" completed. '
    )


if __name__ == "__main__":

    try:
        extract_lines_from_txt(
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/track-Fe1.dat"
            ),
            5,
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/test_01.dat"
            )
        )

        extract_lines_from_csv(
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/VIMD-Fe-Fe-2atom-300k.csv"
            ),
            5,
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/test_02.csv"
            )
        )

        txt_to_csv(
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/track-Fe1.dat"
            ),
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/test_03.csv"
            )
        )
    except FileNotFoundError:
        print("File not found.")
