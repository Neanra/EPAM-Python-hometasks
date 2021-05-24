"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    #remove invalid indexes from the list
    processed_indexes = indexes.copy()
    last = 0
    for index, value in enumerate(processed_indexes):
        if not isinstance(value, int):
            processed_indexes[index] = None
        elif value <= 0:
            processed_indexes[index] = None
        else:
            if value <= last:
                processed_indexes[index] = None
            else:
                last = value
    processed_indexes = list(filter(lambda x: not x is None, processed_indexes))
    
    #split by correct indexes
    previous = 0
    result = []
    for index in processed_indexes:
        if index < len(string):
            result.append(string[previous:index])
            previous = index
        else:
            break
    result.append(string[previous:])
    
    return result
