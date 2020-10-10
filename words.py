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

def cleaned_text(filename):
    """
        Open a file and return a list of words

        filename: file name

        return: list
    """
    # initialize variables
    clean_text = []
    
    # open a file
    fin = open(filename)

    for line in fin:
        stripped_line = line.strip().translate(str.maketrans('', '', string.punctuation)).split()
        for word in stripped_line:
            clean = word.replace(string.punctuation, "").lower()
            clean_text.append(clean)

    # close file
    fin.close()

    return clean_text

if __name__ == "__main__":
    filename = "random_text.txt"
    cleaned = cleaned_text(filename)
    print(cleaned)