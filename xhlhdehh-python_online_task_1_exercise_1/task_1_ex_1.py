"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse


OPS = {
    '+' : getattr(float, "__add__"),
    '-' : getattr(float, "__sub__"),
    '*' : getattr(float, "__mul__"),
    '/' : getattr(float, "__truediv__")
    }

def calculate(args):
    if args.operation in OPS:
        return OPS[args.operation](args.first, args.second)
    else:
        raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description='Performs simple arithmetic \
                                 operations, such as +,-,*,/')
    parser.add_argument("first", type=float, help="First operand")
    parser.add_argument("operation", type=str, help="Operation to perform")
    parser.add_argument("second", type=float, help="Second operand")
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
