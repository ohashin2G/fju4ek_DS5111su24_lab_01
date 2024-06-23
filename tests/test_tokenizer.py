""""
Week 4: Testing
Testing your functions
In the previous lab, you created three functions, clean_text, tokenize and count_words. You wrote them using some of the linux functions as a guide for comparison. Now it is time to formalize what you expect from those functions concretely by creating and definign tests around them.
"""

import sys
import os
import unittest
from collections import Counter
import re
from string import punctuation

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab3 import clean_text, tokenize, count_words



class TestCleanText(unittest.TestCase):
    def test_clean_text(clean_text):
        # GIVEN a string sample_text with words
        text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the clean_text function is called
        trans = str.maketrans('', '', punctuation)
        clean_text = text.lower().translate(trans)
        
        # THEN it should return all lowercase words with no punctuation
        assert isinstance(text, str), f"expected str but got {type(text)}"



class TestTokenize(unittest.TestCase):
    def test_tokenize(tokenize):
        # GIVEN a string clean text
        clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the tokenize function is called
        tokens = re.findall(r'\b\w+\b', clean_text)
        # THEN it should return a python list, where each item is a word in the file
        assert isinstance(tokenize(tokens),
                          list), f'Tokenizer failed on sample text: {clean_text}'



class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        # GIVEN a string clean text
        # WHEN the count_words function is called
        clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        count_words = Counter(clean_text.split())
        len(clean_text.split())
        
        # THEN it should return a dictionary with the words as keys, and their counts as value
        assert count_words,  f"Tokenizer failed on sample text: {clean_text}"



if __name__ == '__main__':
    unittest.main()

# Subsets of Tests
# pytest -v test_tokenizer3.py::TestCleanText::test_clean_text  # single test
# pytest -v test_tokenizer3.py::TestCleanText  # all tests in a class
# pytest -v test_tokenizer3.py::test_function  # single test function
# pytest -v test_tokenizer3.py  # all tests in a file/module
# pytest tests # all tests in a directory

