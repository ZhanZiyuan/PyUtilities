#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pathlib import Path


def insert_line_and_add_number(directory: str,
                               extension: str = ".gjf",
                               index_of_row_to_insert: int = 2,
                               index_to_insert: int = 3,
                               number_to_add: int = 1,
                               print_prompt: bool = True) -> None:
    """
    Modify files in the specified directory
    by inserting a line
    and adding a number to the last row of numbers.

    Parameters
    ----------
    directory: str
        The path to the directory containing files to be modified.
    extension: str
        The file extension to filter files.
        Default is `".gjf"`.
    index_of_row_to_insert: int
        The index of the row to duplicate and insert.
        Default is `2`.
    index_to_insert: int
        The index at which to insert the duplicated row.
        Default is `3`.
    number_to_add: int
        The value to add to the last two numbers in each row.
        Default is `1`.
    print_prompt: bool
        Whether to print a prompt for the modification of each file.
        Default is `True`.

    Returns
    -------
    None

    Examples
    --------
    >>> set_dir_01 = "C:/Users/user/Downloads"
    >>> insert_line_and_add_number(set_dir_01, extension=".log")
    File: "new_01.log" modified.
    File: "new_02.log" modified.
    File: "new_03.log" modified.
    """

    # Traverse all files in the specified directory
    for file_path in Path(directory).iterdir():
        if file_path.suffix == extension:
            # Read each file
            with open(file_path, "r", encoding="utf-8") as read_file_object:
                file_contents = read_file_object.readlines()

            # Insert one duplicate line
            if len(file_contents) > 1:
                file_contents.insert(
                    index_to_insert,
                    file_contents[index_of_row_to_insert]
                )

            # Add `number_to_add` to the last row of numbers
            for line in file_contents:
                if len(line) > 2 and line[0].isdigit() and line[1].isspace():
                    numbers = line.split()
                    numbers[-2] = str(int(numbers[-2]) + number_to_add)
                    numbers[-1] = str(int(numbers[-1]) + number_to_add)
                    line = " ".join(numbers) + "\n"

            # Write the modified contents to the file
            with open(file_path, "w", encoding="utf-8") as write_file_object:
                write_file_object.writelines(file_contents)

                # Whether to print a prompt or not
                if print_prompt:
                    print(
                        f'File: "{file_path.name}" modified. '
                    )
                elif not print_prompt:
                    pass


if __name__ == "__main__":

    set_dir_01 = "C:/Users/user/Downloads"

    try:
        insert_line_and_add_number(
            set_dir_01,
            extension=".log"
        )
    except FileNotFoundError:
        print(
            f'Please check the directory you input: "{set_dir_01}"'
        )
