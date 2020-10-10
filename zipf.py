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

import matplotlib.pyplot as plt

def process_file(filename, skip_header):
    """
        Makes a histogram that contains the words from a file.

        filename: string; file name
        skip_header: boolean; whether to skip the Gutenberg header
   
        return: map from each word to the number of times it appears.
    """
    # initialize variables
    histogram = {}

    # Open the file
    fin = open(filename)

    if skip_header:
        skip_gutenberg_header(fin)

    for line in fin:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, histogram)

    # Close the file
    fin.close()
    return histogram


def skip_gutenberg_header(fin):
    """
        Reads from fp until it finds the line that ends the header.

        fin: open file object
    """
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, histogram):
    """
        Adds the words in the line to the histogram.
        
        ** Modifies histogram. **

        line: string
        histogram: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        histogram[word] = histogram.get(word, 0) + 1


def rank_freq(histogram):
    """
        Returns a list of (rank, freq) tuples.
    
        histogram: map from word to frequency
        
        return: list of (rank, freq) tuples
    """
    # sort the list of frequencies in decreasing order
    freqs = list(histogram.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies 
    ranks_and_frequencies = [(r+1, f) for r, f in enumerate(freqs)]
    return ranks_and_frequencies


def print_ranks(histogram):
    """
        Prints the rank vs. frequency data.
    
        histogram: map from word to frequency
    """
    for r, f in rank_freq(histogram):
        print(r, f)


def plot_ranks(histogram, scale='log'):
    """
        Plots frequency vs. rank.
    
        histogram: map from word to frequency
        scale: string 'linear' or 'log'
    """
    t = rank_freq(histogram)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='the_wendigo.txt', flag='plot'):
    histogram = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(histogram)
    elif flag == 'plot':
        plot_ranks(histogram)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)