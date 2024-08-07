"""Week 3 Lab: python counter, clean, tokenizer"""

#from collections import Counter
import re
#from string import punctuation

CLEANED_TEXT = 'philosophical prose poem of eureka which he deemed the crowning work'


def tokenize(cleaned_text):
    """
    tokenize should take a string and return a python list, where each item is a word in the file.
    Args:
        cleaned_text (str): the clean text to be tokenized
    Returns:
        list: a python list, where each item is a word in the file
    """
    tokens = re.findall(r'\b\w+\b', cleaned_text)
    assert isinstance(tokens, list), f'Tokenizer failed on sample text: {cleaned_text}'
    assert not tokens == "", "should not be empty"
    return tokens




if __name__ == "__main__":
    print(tokenize(CLEANED_TEXT))
