# Week 4: Testing: Testing your functions
# Function: count_words


import sys
import os
import unittest
from collections import Counter
# import re
# from string import punctuation

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
#from src.fju4ek import count_words


class TestCountWords(unittest.TestCase):
    """
    A test case for the count_words function.
        """

    def test_count_words(self):
        """
        Test case for the count_words function.
        GIVEN a string clean text
        WHEN the count_words function is called
        THEN it should return a dictionary with the words as keys, and their counts as value
        """

        clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        count_words = Counter(clean_text.split())
        len(clean_text.split())

        assert count_words, f"Tokenizer failed on sample text: {clean_text}"


if __name__ == '__main__':
    unittest.main()

# Subsets of Tests
# pytest -v test_tokenizer.py::TestCleanText::test_clean_text  # single test
# pytest -v test_tokenizer.py::TestCleanText  # all tests in a class
# pytest -v test_tokenizer.py::test_function  # single test function
# pytest -v test_tokenizer.py  # all tests in a file/module
# pytest tests # all tests in a directory
