"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 13: Case Study: Data Structure Selection in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import string
import random

from bisect import bisect

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


def most_common(histogram):
    """
        Makes a list of word-freq pairs in descending order of frequency.

        histogram: map from word to frequency

        return: list of (frequency, word) pairs
    """
    # initialize variables
    a_list = []
    for key, value in histogram.items():
        a_list.append((value, key))

    a_list.sort()
    a_list.reverse()
    return a_list


def print_most_common(histogram, num=10):
    """
        Print the most commons words in a histgram and their frequencies.
    
        histogram: histogram (map from word to frequency)
        num: number of words to print
    """
    most_common_list = most_common(histogram)
    print('The most common words are:')
    for freq, word in most_common_list[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """
        Identify and return a dictionary with all keys that appear in d1 but not d2.

        d1: dictionaries
        d2: dictionaries

        return: dictionary with all keys that appear in the first dictionary, but not the second
    """
    result = {}
    for key in d1:
        if key not in d2:
            result[key] = None
    return result


def total_words(histogram):
    """
        Total the frequencies in a histogram
        
        histogram: histogram

        return: number
    """
    return sum(histogram.values())


def different_words(histogram):
    """
        Returns the number of different words in a histogram.

        return: number
    """
    return len(histogram)


def random_word(histogram):
    """
        Selects a random word from a histogram. The probability of each word is proportional to its frequency.

        return: string
    """
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in histogram.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


def main():
    hist = process_file('the_wendigo.txt', skip_header=True)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file("words.txt", skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist))


if __name__ == '__main__':
    main()