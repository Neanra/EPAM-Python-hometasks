"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""

import string

def validate_strings(strings):
    for string in strings:
        if not isinstance(string, str):
            raise TypeError


def chars_in_all(*strings):
    validate_strings(strings)
    result = set()
    
    if strings == ():
        return result
    
    for char in strings[0]:
        result.add(char)
    
    letters_to_remove = []
    for string in strings[1:]:
        for char in result:
            if char not in string:
                letters_to_remove.append(char)
        for letter in letters_to_remove:
            result.discard(letter)
    
    return result


def chars_in_one(*strings):
    validate_strings(strings)
    result = set()
    for string in strings:
        for char in string:
            result.add(char)
    return result


def chars_in_two(*strings):
    validate_strings(strings)
    if len(strings) < 2:
        raise ValueError
        
    number_of_occurences = dict()
    letters_in_string = set()
    result = set()
    
    for string in strings:
        for char in string:
            letters_in_string.add(char)
        for letter in letters_in_string:
            number_of_occurences[letter] = number_of_occurences.get(letter, 0) + 1
        letters_in_string = set()
        
    for letter in number_of_occurences:
        if number_of_occurences[letter] >= 2:
            result.add(letter)
            
    return result


def not_used_chars(*strings):
    validate_strings(strings)
    result = set(string.ascii_lowercase)
    for str_ in strings:
        for char in str_:
            result.discard(char)
    return result