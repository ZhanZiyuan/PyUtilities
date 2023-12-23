#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd


def count_numbers(input_file_path: str,
                  column_index: int = 1,
                  lower_limit: Union[int, float] = 0,
                  upper_limit: Union[int, float] = 1,
                  step: float = 0.5,
                  output_file_path: str = "counting_results.csv") -> None:
    """
    Count the occurrences of values within specific ranges
    in a given input CSV file and save the results to a file.

    Args
    ----
        input_file_path (str):
            The path to the input CSV file, which should have no headers.
        column_index (int, optional):
            The index of the column to perform the counting on. Default is 1.
        lower_limit (Union[int, float], optional):
            The lower limit of the range. Default is 0.
        upper_limit (Union[int, float], optional):
            The upper limit of the range. Default is 1.
        step (float, optional):
            The step size between range intervals. Default is 0.5.
        output_file_path (str, optional):
            The path to save the counting results as a CSV file.
            Default is "count_numbers_result.csv".

    Returns
    -------
        None: This function does not return anything.

    Raises
    ------
        FileNotFoundError: If the input_file_path does not exist or is invalid.

    Example
    -------
        count_numbers(
        "input_data.csv", column_index=2, lower_limit=0, upper_limit=10, step=1, output_file_path="result.csv"
        )
    """
    df = pd.read_csv(input_file_path, header=None)  # The input `.csv` should have no headers.

    gap_ranges = [
        (i, i + step)
        for i in np.arange(lower_limit, upper_limit, step)
    ]

    counts = []
    for start, end in gap_ranges:
        filtered_df = df[
            (df.iloc[:, column_index] >= start)
            & (df.iloc[:, column_index] < end)
        ]  # left-closed, right-open interval
        counts.append(len(filtered_df))

    result_df = pd.DataFrame(
        {
            'Lower Limit': [start for start, _ in gap_ranges],
            'Upper Limit': [end for _, end in gap_ranges],
            'Count': counts
        }
    )
    print(result_df)

    result_df.to_csv(output_file_path, index=False)
    print(f'Results of counting saved to: "{Path(output_file_path).name}"')


def get_max_value(input_file_path: str,
                  column_index: int) -> None:
    """
    Get the maximum value from a specific column in a given input CSV file.

    Args
    ----
        input_file_path (str):
            The path to the input CSV file, which should have no headers.
        column_index (int):
            The index of the column to find the maximum value.

    Returns
    -------
        None: This function does not return anything.

    Raises
    ------
        FileNotFoundError: If the input_file_path does not exist or is invalid.

    Example
    -------
        get_max_value("input_data.csv", column_index=2)
    """
    df = pd.read_csv(input_file_path, header=None)
    print(f"The maximum is: {df.iloc[:, column_index].max()}")


def get_min_value(input_file_path: str,
                  column_index: int) -> None:
    """
    Get the minimum value from a specific column in a given input CSV file.

    Args
    ----
        input_file_path (str):
            The path to the input CSV file, which should have no headers.
        column_index (int):
            The index of the column to find the minimum value.

    Returns
    -------
        None: This function does not return anything.

    Raises
    ------
        FileNotFoundError: If the input_file_path does not exist or is invalid.

    Example
    -------
        get_min_value("input_data.csv", column_index=2)
    """
    df = pd.read_csv(input_file_path, header=None)
    print(f"The minimum is: {df.iloc[:, column_index].min()}")


if __name__ == "__main__":

    try:
        file_path = (
            "/home/zhanziyuan/python_assignments"
            "/2023.03/utilities/count_numbers"
            "/VIMD-Fe-Fe-2atom-300k.csv"
        )

        count_numbers(
            file_path,
            1, 0, 20, 2,
            (
                "/home/zhanziyuan/python_assignments"
                "/2023.03/utilities/count_numbers"
                "/counting_results.csv"
            )
        )

        get_max_value(file_path, 1)

        get_min_value(file_path, 1)
    except FileNotFoundError:
        print("File not found.")
