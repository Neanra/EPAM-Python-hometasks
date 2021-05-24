"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = None) -> list:
    if not isinstance(str_to_split, str):
        raise ValueError
    result = []
    if str_to_split is '':
        return result
    
    accumulator = ''
    if delimiter is None:
        str_to_split = str_to_split.strip()
        i = 0
        flush = False
        while i < len(str_to_split):
            while len(str_to_split) > i and str_to_split[i].isspace():
                i += 1
                flush = True
            if flush:
                result.append(accumulator)
                accumulator = ''
                flush = False
            accumulator += str_to_split[i]
            i += 1
        result.append(accumulator)
        return result
            
    accumulator = ''
    for char in str_to_split:
        if char == delimiter:
            result.append(accumulator)
            accumulator = ''
        else:
            accumulator += char
    result.append(accumulator)
    return result
