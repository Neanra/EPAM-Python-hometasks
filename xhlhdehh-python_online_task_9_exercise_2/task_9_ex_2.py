"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError
    filtered_string = "".join(filter(lambda x: x.isalpha(), test_string))
    reversed_string = "".join(reversed(filtered_string))
    return reversed_string.upper() == filtered_string.upper()
    
    
