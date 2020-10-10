"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 13: Case Study: Data Structure Selection in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
from __future__ import print_function, division

import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """
        Reads a file and performs Markov analysis.
    
        filename: string
        order: integer number of words in the prefix
        
        return: map from prefix to list of possible suffixes.
    """
    # open the file
    fin = open(filename)
    skip_gutenberg_header(fin)

    for line in fin:
        if line.startswith('*** END OF THIS'): 
            break

        for word in line.rstrip().split():
            process_word(word, order)
    
    # close the file
    fin.close()


def skip_gutenberg_header(fin):
    """
        Read from a file until it finds the line that ends the header.
    
        fin: open file object
    """
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break


def process_word(word, order=2):
    """
        Store the words into the global variable 'prefix' and then add entries to the dictionary
        
        word: string
        order: integer
        
        During the first few iterations, all we do is store up the words; after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """
        Generates random wordsfrom the analyzed text. Starts with a random prefix from the dictionary.
        
        n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def shift(t, word):
    """
        Forms a new tuple by removing the head and adding word to the tail.
    
        t: tuple of strings
        word: string
        
        return: tuple of strings
    """
    return t[1:] + (word,)


def main(script, filename='the_wendigo.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else: 
        process_file(filename, order)
        random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)