"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""

import argparse

NUM = {
           "I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100
           }

def analyze_roman(s):
    l_substr = []
    work_str = s[::-1]
    k = 0
    while k < len(work_str):
        substr = ''
        print('stage', k, work_str[k])
        if k > 0 and s[k] < s[k-1]:
            substr += s[k-1]
            print(substr)
            i = k
            while s[i] < s[i-1]: 
                substr += s[i]
                print(substr)
        k += 1
        l_substr.append(substr)
    print(l_substr)

def from_roman_numerals(args):
    result = 0
    previous = None
    for n in args.rnum[::-1]:
        if not n in NUM:
            raise ValueError
        if previous and NUM[n] < previous:
            result -= NUM[n]
        else:
            result += NUM[n]
        previous = NUM[n]
    if result > 100 or result < 0:
        raise ValueError
    return result


def main():
    parser = argparse.ArgumentParser(description='Converts a Roman number into an \
                                 Arabic numeral')
    parser.add_argument("rnum", type=str, help="Roman number")                              
    args = parser.parse_args()

    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
