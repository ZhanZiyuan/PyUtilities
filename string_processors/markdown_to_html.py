from pathlib import Path

from markdown import markdown


def markdown_to_html(markdown_path: str,
                     html_path: str,
                     print_prompt: bool = True) -> None:
    """
    Convert the Markdown file to a HTML file.
    """
    with open(markdown_path, 'r', encoding='utf-8') as markdown_read_object:
        markdown_contents = markdown_read_object.read()

    html_contents = markdown(markdown_contents)

    with open(html_path, 'w', encoding='utf-8') as html_write_object:
        html_write_object.write(html_contents)

    if print_prompt:
        print(
            f'Converted the input Markdown file: "{Path(markdown_path).name}" '
            f'to the HTML file: "{Path(html_path).name}". '
        )
    elif not print_prompt:
        pass


if __name__ == "__main__":

    try:
        markdown_to_html(
            markdown_path="C:/Users/user/Downloads/input.md",
            html_path="C:/Users/user/Downloads/output.html"
        )
    except FileNotFoundError:
        print(
            "Please check the path of the input file "
            "or that of the output file. "
        )
