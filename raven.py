"""
Test cases for the raven module.
Get repeatable results. What I mean is that we are now going to fix which files are used in testing so we compare apples to apples.

17192 The Raven
932 Fall of the House of Usher
1063 Cask of Amontillado
10031 The Poems
14082 And Le Corbeau. So we see how the tokenizer stands up to accented characters.
"""

from collections import Counter

def tokenize(somestr):
	# GIVEN a string text
	
    book_ids = ("17192", "932", "1063", "10031", "14082")
    all_text = ""
    # Loop through `book_ids` and download each book
    for id in book_ids: 
       url = f"https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
	
 	# WHEN the count_words function is called
    words = all_text.split()
    count_words = Counter(words)
    return len(somestr.split())   

    # THEN it should return a dictionary with the words as keys, and their counts as value
    assert count_words,  f"Tokenizer failed on sample text: {words}"
    

