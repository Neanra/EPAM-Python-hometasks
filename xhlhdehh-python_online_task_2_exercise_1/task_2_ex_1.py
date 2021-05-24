# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:40:46 2021

@author: Julia Issajeva
"""


"""
Task 2_1

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""

import argparse

def bounded_knapsack(args):
    if args.bars_number != len(args.weights):
        raise ValueError
        
    if not all(map(lambda x: x >= 0, args.weights)) or args.capacity < 0:
        raise ValueError
        
    args.weights.sort()
    free_space = args.capacity
    while len(args.weights) != 0:
        bar = args.weights.pop()
        if bar <= free_space:
            free_space -= bar
    return args.capacity - free_space

def main():
    parser = argparse.ArgumentParser(description="Determines the max weight of \
                                 bars that fit into the given sack");

    parser.add_argument("-W", type=int, dest="capacity", help="Max weight",
                        required=True)
    parser.add_argument("-w", type=int, nargs="*", dest="weights", help="Bars weights",
                        required=True)
    parser.add_argument("-n", type=int, dest="bars_number", help="Bars count",
                        required=True)
    
    args = parser.parse_args();
    
    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
