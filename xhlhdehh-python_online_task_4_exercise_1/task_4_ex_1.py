"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    str_list = []
    for char in string:
        if char == "'":
            str_list.append('"')
        elif char == '"':
            str_list.append("'")
        else:
            str_list.append(char)
    return ''.join(str_list)