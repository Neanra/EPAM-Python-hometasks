"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    #raise RuntimeError(n, type(n))
    if type(n) == bool:
        raise TypeError
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise TypeError
    result = 0
    for digit in str(n):
        if int(digit) % 2 == 1:
            result += int(digit)
    return result