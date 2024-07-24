"""Week 3 Lab: python counter, clean, tokenizer"""

#from collections import Counter
#import re
from string import punctuation

SAMPLE_TEXT = 'philosophical prose poem of eureka which he deemed the crowning work'


def clean_text(sample_text):
    """
    clean_text, should take a string, and should return all lowercase words, 
    and throw out any punctuation

    Args:
        text (str): the sample text to be cleaned

    Returns:
        words: all lowercase words with no puctuation
    """
    assert isinstance(
        sample_text, str), f"expected str but got {type(sample_text)}"

    trans = str.maketrans('', '', punctuation)
    assert not isinstance(trans, int)

    cleaned_text = sample_text.lower().translate(trans)
    assert isinstance(cleaned_text, str)
    assert not cleaned_text == "", "should not be empty"
    return cleaned_text



if __name__ == "__main__":
    print(clean_text(clean_text(SAMPLE_TEXT)))
