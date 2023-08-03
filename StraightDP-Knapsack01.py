#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
* Title: 0/1 Knapsack Problem Solver 
* Author : Emre Akgül 
* Description : 0/1 Knapsack Problem solver that uses straight forward dynamic programming method.
* Main method and data cleaning stages are written by Discrete Optimization course on Coursera provided by The University of Melbourne.
* Course URL: https://www.coursera.org/learn/discrete-optimization
"""

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
def KnapsackSolver(input_data):
    """
    inputs:
        input_data = file name that includes data
    outputs:
        optimal_solution = optimal solution to the given 0/1 knapsack problem 
        is_taken = show which items are taken in optimal solution


    Input data format:
        First line format  "number_of_items knapsack_capacity"
        Other lines format "value_of_item weight_of_item"  
    Example data:
        3 9
        5 4
        6 5
        3 2
    """

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    

    # Algorithm starts here.

    optimal_solution = 0
    is_taken = [False]*len(items)
    # Uses straight forward dynamic programming algorithm for solving 0/1 knapsack problem.
    cache = [[0 for x in range(capacity + 1)] for x in range(item_count + 1)]
    for i in range(1, item_count + 1):
        for j in range(1, capacity + 1):
            if j - items[i-1].weight < 0:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i-1][j - items[i-1].weight] + items[i-1].value)
    
    x = item_count
    y = capacity
    optimal_solution = cache[x][y]

    # Backtracks on cache for finding taken items.
    while(x > 0):
        if cache[x][y] != cache[x-1][y]:
            y -= items[x-1].weight
            is_taken[x-1] = True
        x-=1


    return optimal_solution, is_taken


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(KnapsackSolver(input_data))
    else:
        print('This test requires an input file.')

