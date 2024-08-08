from fju4ek.count_words import count_words
import sys
import os
import pytest
from collections import Counter

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.parametrize(
    "count_words",
    [
        ("clean text", "done"),
        ("count words", "done"),
        ("tokenize words", "done"),
    ],
)
def test_finish(clean_text, count_words):
	clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
	count_words = Counter(clean_text.split())
	len(clean_text.split())
	return clean_text, count_words

    assert count_words, f"Tokenizer failed on sample text: {clean_text}"


@pytest.mark.parametrize("clean_text, tokenizer", ["done", " in prog", "todo"])
def test_finish_simple(clean_text, count_words):
    clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    count_words = Counter(clean_text.split())
    len(clean_text.split())

    assert count_words, f"Tokenizer failed on sample text: {clean_text}"


if __name__ == '__main__':
    pass
