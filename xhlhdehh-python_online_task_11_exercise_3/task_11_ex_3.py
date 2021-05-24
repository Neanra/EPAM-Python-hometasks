"""
Task 3

Implement a decorator `call_once` which runs `sum_of_numbers` function once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

Example:
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

>>> 55

print(sum_of_numbers(999, 100))

>>> 55

print(sum_of_numbers(134, 412))

>>> 55
"""

def call_once(f):
    cache = None
    def wrapper(*args):
        nonlocal cache
        if not cache:
            cache = f(*args)
        return cache
    return wrapper
            

@call_once
def sum_of_numbers(a, b):
    return a + b
