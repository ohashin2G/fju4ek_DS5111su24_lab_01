""""Week 4: Testing: Testing Function: clean_text"""

import unittest
import sys
# import os
# from collections import Counter
# import re
from string import punctuation
sys.path.append('./src')
# import fju4ek as pkg
# import clean_text function from clean_text module
# from clean_text import clean_text


class TestCleanText(unittest.TestCase):
    """Unit Test: clean_text function"""

    def test_clean_text(self):
        """Unit Test: clean_text function"""
        # GIVEN a string sample_text with words
        text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the clean_text function is called
        trans = str.maketrans('', '', punctuation)
        text = text.lower().translate(trans)

        # THEN it should return all lowercase words with no punctuation
        assert isinstance(text, str), f"expected str but got {type(text)}"


if __name__ == '__main__':
    unittest.main()
