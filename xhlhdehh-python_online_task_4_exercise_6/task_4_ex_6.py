"""
Task04_6

Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (`,\n,\tand so on).
If there are multiple longest words in the string with a same length return the word that occurs first.

Example: get_longest_word('Python is simple and effective!')
         #output: 'effective!'
         get_longest_word('Any pythonista like namespaces a lot.')
         #output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is prohibited
"""


def get_longest_word(str_to_parse: str) -> str:
    #raise RuntimeError(str_to_parse)
    if not isinstance(str_to_parse, str):
        raise ValueError
    split_string = str_to_parse.split()
    #raise RuntimeError(split_string)
    longest = split_string[0]
    for word in split_string:
        if len(word) > len(longest):
            longest = word
    #raise RuntimeError(longest)
    return longest

