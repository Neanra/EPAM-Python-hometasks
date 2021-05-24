""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""

import argparse
import operator

OPS = {
       '+': operator.add,
       '-': operator.sub
      }

def check_formula(user_input):
    accumulator = []
    num = ''
    result = True
    
    if user_input == '':
        return (False, None)
    
    #transforming user input string into list with integers and functions
    for char in user_input:
        if char not in OPS:
            if char.isdigit():
                num += char
            #the char is not valid (digit or sign)
            else: 
                result = False
                break
        else:
            #this only occurs in invalid strings, when it is two signs a row
            if num == '':
                result = False
                break
            #putting a number into accumulator (we know for sure right now that
            #all chars in num are digits)
            accumulator.append(int(num))
            num = ''
            accumulator.append(OPS[char])
    #if num == '' then sign is the last in the string and this is invalid
    if result and num != '':
        accumulator.append(int(num))
        
    if result:
        #sign is the first and this is invalid
        if not isinstance(accumulator[0], int):
            result = False
        else:
            total = accumulator.pop(0)
            while accumulator != []:
                try:
                    #elements should go in sign-number pairs if input is valid
                    f = accumulator.pop(0)
                    operand = accumulator.pop(0)
                    if isinstance(operand, int):
                        total = f(total, operand)
                    else:
                        result = False
                        break
                except IndexError:
                    result = False
                    break
    if not result:
        total = None
    return (result, total)


def main():
    parser = argparse.ArgumentParser(description='Performs standart math functions')
    parser.add_argument("user_input", type=str, help="EBNF input string")                              
    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
