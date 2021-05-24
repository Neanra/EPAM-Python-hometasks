"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


def sum_binary_1(n: int):
    if not isinstance(n, int):
        return None
    if n <= 0:
        return None
    result = 0
    for digit in bin(n)[2:]:
        if digit == '1':
            result += 1
    return result
