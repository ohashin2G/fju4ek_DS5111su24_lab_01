"""Week 3 Lab: python counter, clean, tokenizer"""

#from collections import Counter
#import re
#from string import punctuation

CLEANED_TEXT = "philosophical prose poem of eureka which he deemed the crowning work"


def count_words(cleaned_text):
    """
    Count_words should take a string and return a dictionary with the words 
    as keys, and their counts as value

    Args:
        text(str): the sample text to be counted
    Returns:
        dict: a dictionary with the words as keys, and their counts as value
    """

    word_counts = {}
    for word in cleaned_text.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    assert isinstance(word_counts, dict)

    # word_counts.most_common(2)  # Commented out as it is not used in the code

    assert isinstance(list(word_counts.items()), list)

    assert isinstance(sum(word_counts.values()), int)

    return len(word_counts)


if __name__ == "__main__":
    print(count_words(CLEANED_TEXT))
