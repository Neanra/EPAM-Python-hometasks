"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*dict_tuple):
    #raise RuntimeError(dict_tuple)
    result = {}
    for dict_ in dict_tuple:
        for key, value in dict_.items():
            if not (isinstance(key, str) and len(key) == 1 and key.isalpha()):
                raise KeyError
            if not isinstance(value, int):
                raise ValueError
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
    
