"""
Week 4: Testing
Testing your functions
Function: tokenize

"""

import sys
import os
import unittest
from collections import Counter
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('./src/pkg_fju4ek')
from src.fju4ek.tokenizer import tokenize



class TestTokenize2(unittest.TestCase):
	"""unittest: tokenizes a string of clean text into a list of words
		Args:
			clean_text (str): a string of clean text
		Returns:
			list: a list of words
		Example:
			>>> clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
			>>> tokenize(clean_text)
			['But', 'the', 'Raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'That', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour']
		"""

	def test_tokenize(self):
        # GIVEN a string clean text
		cleaned_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the tokenize function is called
		tokens = re.findall(r'\b\w+\b', cleaned_text)
        # THEN it should return a python list, where each item is a word in the file
		assert isinstance(
            tokens, list), f'Tokenizer failed on sample text: {cleaned_text}'


class TestTokenize(unittest.TestCase):
    def test_tokenize(self):
        # GIVEN a string clean text
        cleaned_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the tokenize function is called
        tokens = re.findall(r'\b\w+\b', cleaned_text)
        # THEN it should return a python list, where each item is a word in the file
		
        assert isinstance(tokenize(cleaned_text),
				  list), f'Tokenizer failed on sample text: {cleaned_text}'


class TestCountWords(unittest.TestCase):
    def test_count_words(self):
		# GIVEN a string clean text
		# WHEN the count_words function is called
        cleaned_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        count_words = Counter(cleaned_text.split())
        len(cleaned_text.split())

        # THEN it should return a dictionary with the words as keys, and their counts as value
        assert count_words,  f"Tokenizer failed on sample text: {cleaned_text}"


if __name__ == '__main__':
    unittest.main(exit=False)


# Subsets of Tests
# pytest -v test_tokenizer.py::TestCleanText::test_clean_text  # single test
# pytest -v test_tokenizer.py::TestCleanText  # all tests in a class
# pytest -v test_tokenizer.py::test_function  # single test function
# pytest -v test_tokenizer.py  # all tests in a file/module
# pytest tests # all tests in a directory
