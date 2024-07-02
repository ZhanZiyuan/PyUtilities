#!/usr/bin/env python
# -*- coding:utf-8 -*-


def replace_text(input_file_path: str,
                 output_file_path: str,
                 replacements: dict) -> None:
    """
    Replace specified strings in a text file
    and save the result to a new file.

    Parameters
    ----------
    input_file_path: str
        The path to the input text file.
    output_file_path: str
        The path to the output text file
        where the modified content will be saved.
    replacements: dict
        A dictionary where keys are strings to be replaced
        and values are the new strings to replace them with.
    """
    with open(input_file_path, "r", encoding="utf-8") as file_object_read:
        file_contents = file_object_read.read()

    for old_string, new_string in replacements.items():
        # NOTE:
        # `file_contents` is assigned to itself to change its value
        # for strings are unchangeable
        # and `replace()` will not change the original string.
        file_contents = file_contents.replace(old_string, new_string)

    with open(output_file_path, "w", encoding="utf-8") as file_object_written:
        file_object_written.write(file_contents)


def insert_text(file_to_insert: str,
                line_number: int,
                text_to_insert: str,
                indent: int = 8,
                add_line_feed: bool = False) -> None:
    """
    __doc__
    """

    with open(file_to_insert, "r", encoding="utf-8") as file_object_read:
        lines = file_object_read.readlines()

    if 1 <= line_number <= len(lines):
        if add_line_feed:
            indented_text = " " * indent + text_to_insert + "\n"
        else:
            indented_text = " " * indent + text_to_insert
        lines.insert(line_number - 1, indented_text)
    else:
        raise IndexError(
            f'The line number "{line_number}" '
            'is out of range. '
        )

    with open(file_to_insert, "w", encoding="utf-8") as file_object_written:
        file_object_written.writelines(lines)


def remove_text(file_to_remove_text: str,
                line_number: int,
                add_line_feed: bool = True) -> None:
    """
    Removes a line of text at the specified line number from the given file.
    """

    with open(file_to_remove_text, "r", encoding="utf-8") as file_object_read:
        lines = file_object_read.readlines()

    if 1 <= line_number <= len(lines):
        lines.pop(line_number - 1)
        if add_line_feed:
            lines.insert(line_number - 1, "\n")
        else:
            pass
    else:
        raise IndexError(
            f'The line number "{line_number}" '
            'is out of range. '
        )

    with open(file_to_remove_text, "w", encoding="utf-8") as file_object_written:
        file_object_written.writelines(lines)


if __name__ == "__main__":

    original_file_path = "C:/Users/user/Downloads/original.py"
    replaced_file_path = "C:/Users/user/Downloads/replaced.py"

    strings_to_replace = {
        "con_0_": "0.1000",
        "con_1_": "0.2000",
        "con_2_": "0.3000",
        "con_3_": "0.4000",
    }

    replace_text(
        input_file_path=original_file_path,
        output_file_path=replaced_file_path,
        replacements=strings_to_replace
    )

    path_of_file_to_insert = "C:/Users/user/Downloads/insert.py"
    new_text_to_insert = "hello mike"

    insert_text(
        file_to_insert=path_of_file_to_insert,
        line_number=24,
        text_to_insert=new_text_to_insert,
        indent=8,
        add_line_feed=False
    )

    remove_text(
        file_to_remove_text=path_of_file_to_insert,
        line_number=24,
        add_line_feed=True
    )
