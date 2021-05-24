"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    if not isinstance(input_file_path, str) or not isinstance(output_file_path, str):
        raise TypeError
        
    list_of_names = []
    with open(input_file_path, 'r') as input_handle:
        for line in input_handle:
            list_of_names.append(line)
    list_of_names.sort()
    with open(output_file_path, 'w', encoding = 'utf-8') as output_handle:
        for line in list_of_names:
            output_handle.write(line)
