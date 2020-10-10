"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 13: Case Study: Data Structure Selection in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import random

def choose_from_hist(histogram):
    """
        Return a random value from a histogram

        histogram: histogram

        return: random value from the histogram
    """
    # initialize values
    rando = random.uniform(0, 1)
    s = 0
    a_dictionary = {}
    cumulative_probability = 0

    for val in histogram.values():
        s += val
    
    for key, val in histogram.items():
        a_dictionary[key] = val/s
    
    for key, val in a_dictionary.items():
        cumulative_probability += val
        if rando < cumulative_probability:
            break
    return key

def histogram(my_string):
    """
        Count apperance of the letters in the string.

        my_string: string

        return: dictionary
    """
    # initialize values
    a_dictionary = dict()
    for c in my_string:
        a_dictionary[c] = a_dictionary.get(c, 0) + 1
    return a_dictionary


if __name__ == "__main__":
    print(histogram("apple"))
    print(choose_from_hist(histogram("apple")))