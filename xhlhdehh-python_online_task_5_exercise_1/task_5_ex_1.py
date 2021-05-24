"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""

from enum import Enum

class SortOrder(Enum):
    ascending = 0
    descending = 1


def is_sorted(num_list, sort_order: SortOrder) -> bool:
    #raise RuntimeError(num_list, sort_order)
    
    #check if all arguments are valid
    if not isinstance(num_list, list) or not isinstance(sort_order, SortOrder):
        raise TypeError
    for item in num_list:
        if type(item) != int:
            raise TypeError
    
    #define comparator
    if sort_order == SortOrder.ascending:
        f = lambda first, second: first > second
    if sort_order == SortOrder.descending:
        f = lambda first, second: first < second
    
    #determine whether a given list of integer values is sorted in a given order
    previous = None
    for item in num_list:
        if previous:
            if not f(previous, item):
                return False
        previous = item
    return True

def transform(num_list, sort_order: SortOrder):
    if not is_sorted(num_list, sort_order):
        return num_list
    else:
        return [item + index for index, item in enumerate(num_list)]
