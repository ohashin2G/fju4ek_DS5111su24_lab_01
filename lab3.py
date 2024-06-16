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

sample_text = """
And he looked over at the alarm clock, ticking on the chest of drawers. "God in Heaven!" he thought. It was half past six and the hands were quietly moving forwards, it was even later than half past, more like quarter to seven. Had the alarm clock not rung? He could see from the bed that it had been set for four o'clock as it should have been; it certainly must have rung. Yes, but was it possible to quietly sleep through that furniture-rattling noise? True, he had not slept peacefully, but probably all the more deeply because of that.
"""

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


