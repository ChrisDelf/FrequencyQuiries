#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    freq_dict = defaultdict(int)
    value_dict = defaultdict(int)
    results_array = []

    for command, value in queries:
        

        # when we add a number to our data strucuture
        if command == 1:

            if value in value_dict:
                # redue the values's old count      
                if freq_dict[value_dict[value]] > 0:
                    freq_dict[value_dict[value]] -= 1
            
                value_dict[value] +=1
                # adding the values' new count
                freq_dict[value_dict[value]] += 1
            # if not in our value dictionary
            else:
                # instantiate the values new count
                value_dict[value] = 1

                # if its already in the freq count then increment
                if freq_dict[value_dict[value]]:
                    freq_dict[value_dict[value]] += 1
                else:
                # if not instantiate it
                    freq_dict[value_dict[value]] = 1
                    
        # when we remove a number from our data strucutre        
        if command == 2:
            if value_dict[value]:
                freq_dict[value_dict[value]] -= 1

                value_dict[value] -=1

                freq_dict[value_dict[value]] += 1
        # checking for frequcny
        if command == 3:

            if value in freq_dict and freq_dict[value] > 0:
                results_array.append(1)
            else:
                results_array.append(0)
    return results_array
