"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError
    str_list = []
    for char in test_string:
        if char.isalpha():
            str_list.append(char)
    s = ''.join(str_list)
    s = s.upper()
    if s == '':
        return True
    index = 0
    while index <= len(s) - 1 - index:
        if not s[index] == s[len(s) - 1 - index]:
            return False
        index += 1
    return True