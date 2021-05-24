"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse
import operator
import math

def calculate(args):
    for m in [math, operator]:
        try:
            f = getattr(m, args.function)
            return f(*map(float, args.params))
        except AttributeError:
            pass
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description='Performs standart math functions')

    parser.add_argument("function", type=str, help="Function to perform")
    parser.add_argument("params", nargs = "*")
                                     
    args = parser.parse_args()
    
    print(calculate(args))


if __name__ == '__main__':
    main()
