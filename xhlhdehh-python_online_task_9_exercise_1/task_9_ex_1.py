"""
Task_9_1
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(some_string: str) -> str:
    #FDD0 - sentinel symbol
    result = some_string.replace('\'', '\xFDD0').replace('\"', '\'').replace('\xFDD0', '\"')
    return result
