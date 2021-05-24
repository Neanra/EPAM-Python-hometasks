"""
Implement a function get_longest_word(s: str) -> str which returns the
longest word in the given string. The word can contain any symbols
except whitespaces (`,\n,\t and so on). If there are multiple longest
words in the string with a same length return the word that occurs first.

Example:
get_longest_word('Python is simple and effective!')
#output: 'effective'
get_longest_word('Any pythonista like namespaces a lot.')
#output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is required.
"""

import re
import functools

def get_longest_word(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError
    return functools.reduce(lambda x, y: x if len(x) >= len(y) else y, re.findall('\w+',s))