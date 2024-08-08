# Week 4: Testing: Testing your functions
# Function: count_words


import sys
import os
import pytest
from collections import Counter
# import re
# from string import punctuation

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
#from src.fju4ek import count_words



"""
A test case for the count_words function.
"""
# Allan Poe's The Raven

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

# Carbeau
corbeau = ("""_Mais le Corbeau, perché solitairement sur ce buste placide, parla
ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
que je fis à peine davantage que marmotter «D'autres amis déjà ont
pris leur vol--demain il me laissera comme mes Espérances déjà ont
pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_""")

@pytest.mark.skip(reason="French text will be replaced with Japanese text when it's ready")
def test_count_words(self):
    """
    Test case for the count_words function.
    GIVEN a string clean text
    WHEN the count_words function is called
    THEN it should return a dictionary with the words as keys, and their counts as value
    """

    clean_text = corbeau
    count_words = Counter(clean_text.split())
    len(clean_text.split())

    assert not clean_text == "", "should not be empty"
    assert isinstance(
        count_words, dict), f"expected dict but got {type(count_words)}"
    assert count_words,  f"Tokenizer failed on sample text: {clean_text}"


clean_text = corbeau
@pytest.mark.parametrize("clean_text, expected_count_words", [
    (clean_text, corbeau),
])

def test_count_words_all(clean_text, expected_count_words):
	"""
	Test case for the count_words function.
	GIVEN a string clean text
	WHEN the count_words function is called
	THEN it should return a dictionary with the words as keys, and their counts as value
	"""
	count_words = Counter(clean_text.split())
	#assert count_words == expected_count_words, f"Tokenizer failed on sample text: {clean_text}"
	assert not clean_text == "", "should not be empty"
	assert isinstance(
		count_words, dict), f"expected dict but got {type(count_words)}"
	assert count_words,  f"Tokenizer failed on sample text: {clean_text}"

	corbeau_counts = Counter(corbeau.split())
	#assert corbeau_counts == expected_count_words, f"Tokenizer failed on sample text: {corbeau}"


if __name__ == '__main__':
    pass


# Subsets of Tests
# pytest -v test_tokenizer.py::TestCleanText::test_clean_text  # single test
# pytest -v test_tokenizer.py::TestCleanText  # all tests in a class
# pytest -v test_tokenizer.py::test_function  # single test function
# pytest -v test_tokenizer.py  # all tests in a file/module
# pytest tests # all tests in a directory
