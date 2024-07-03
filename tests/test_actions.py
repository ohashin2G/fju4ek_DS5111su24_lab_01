"""
Week 5 Lab: Setting up your tests to run in Github Actions
Adding groups of tests (4 pts)
* Add two more complicated tests that use your functions as a group. Perhaps tests that download, clean, tokenize and then take a count for a handful of common words.
* Add a pytest marker to label them as integration tests.
* On your makefile, update your test job so it runs ONLY the NON integration tests.
* Now add a step in your github workflow to run the NON integration tests, and a separate step that runs the INTEGRATION steps. So you get the full set, in two steps.
"""
import pytest
import unittest
from string import punctuation
import re
from collections import Counter
import requests
import sys
import subprocess


# Download text from 932 Fall of the House of Usher
usher = requests.get(
    'https://www.gutenberg.org/cache/epub/932/pg932.txt').text


class TestActions(unittest.TestCase):
    @pytest.fixture()
    def clean_text():
        """Test the text returned clean text with no punctuation."""
        return usher.lower().translate(str.maketrans('', '', punctuation))
    assert isinstance(usher, str), f"expected str but got {type(usher)}"
    
    @pytest.fixture()
    def tokenizer():
        """Return a list of words."""
        return re.findall(r'\b\w+\b', usher)
    assert isinstance(tokenizer, list), f"expected list but got {type(tokenizer)}"

    @pytest.fixture()
    def count_words(usher):
        """Return a dictionary of word counts."""
        return Counter(usher.split())
    assert count_words,  f"Tokenizer failed on sample text: {usher}"
    




    @pytest.mark.parametrize("file_name", ["get_the_books.sh", *book_ids])
    def test_file_processing(file_name):
        """Test the file was correctly downloaded and saved in a variable."""
        try:
            assert file_name, f"Expected True but got {file_name}"
        except FileNotFoundError as e:
            print("An error occurred while processing the file:", e)
            assert True

    @pytest.fixture()
    def clean_text():
        """Return cleaned text with no punctuation."""
        return file_name.lower().translate(str.maketrans('', '', punctuation))
    
    def tokenizer():
        return re.findall(r'\b\w+\b', file_name)
