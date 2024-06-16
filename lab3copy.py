"""
Week 3 Lab: python counter, cleaner, tokenizer

Functions:
- clean_text: should take a string, and should return all lowercase words,
and throw out any punctuation
- tokenize: should take a string and return a python list, where each item is
a word in the file
- count_words: should take a string and return a dictionary with the words 
as keys, and their counts as value
"""

from collections import Counter
import re
from string import punctuation
import wget

sample_text = wget.download('https: // www.gutenberg.org/cache/epub/17192/pg17192.txt')
#sample_text = get_the_books.sh

def clean_text(sample_text):
    """
    clean_text, should take a string, and should return all lowercase words, 
 	and throw out any punctuation

	Args:
		text (str): the sample text to be cleaned

	Returns:
		words: where each item is a word in the file
	"""
    trans = str.maketrans('', '', punctuation)
    clean_text = sample_text.lower().translate(trans)
    return clean_text

print(clean_text(sample_text))

def tokenize(clean_text):
    """
	tokenize should take a string and return a python list, where each item is a word in the file.
	Args:
		text (str): the sample text to be tokenized
	Returns:
		list: a python list, where each item is a word in the file
 	"""
    tokens = re.findall(r'\b\w+\b', clean_text)
    return tokens

print(tokenize(clean_text(sample_text)))

def count_words(clean_text):
    """
	Count_words should take a string and return a dictionary with the words as keys,
 	and their counts as value

	Args:
		text(str): the sample text to be counted
	Returns:
		dict: a dictionary with the words as keys, and their counts as value
	"""
    
    txt = clean_text
    count_words = Counter(txt.split())
    count_words.most_common(2) 
    sum(count_words.values())
    return count_words

print(count_words(clean_text(sample_text)))
print(count_words(clean_text(sample_text)).most_common(2))
print(sum(count_words(clean_text(sample_text)).values()))

# Alternatively using loop
for word, count in count_words(clean_text(sample_text)).items():
	print(word, count)


# Check inputs to functions
assert isinstance(clean_text(sample_text), str)
assert isinstance(tokenize(clean_text(sample_text)), list)
assert isinstance(count_words(sample_text), dict)

# Check return types


