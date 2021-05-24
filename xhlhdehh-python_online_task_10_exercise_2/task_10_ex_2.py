"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""

import re

def most_common_words(text, top_words):
    if not isinstance(text, str):
        raise TypeError
    if type(top_words) is not int:
        raise TypeError
    
    top_count = dict()
    with open(text, 'r') as file_handle:
        for line in file_handle:
            for word in re.findall('\w+', line):
                top_count[word] = top_count.get(word, 0) + 1
    
    result = []
    for k, v in sorted(top_count.items(), key = lambda x: x[1], reverse=True)[:top_words]:
        result.append(k)
    return result