import random
import re

from wordify import load_corpus
from constants import SENTENCES

# Precompilation of the regex so that it would not have to be compiled
# every iteration, saving time overall
FORMAT_STR = re.compile("{(.*?)}")

# Possible sentence constructions. As we go along, can add many more
# and then divide them into beginning, body and end constructions,
# allowing for a wider variety of sentences.

corpus = load_corpus()


def non_numeric_string(string: str) -> str:
    """Return a string without embedded numeric characters."""
    return "".join(char for char in string if not char.isdigit())


def write_sentence(n: int) -> str:
    """Given a line number returns one of the possible poem sentence
     constructions, filled with random words from the wordlists.
    """

    # Picks the base sentence
    base_sentence = SENTENCES[n % len(SENTENCES)]

    # Creates a dictionary where the given category is matched up to the
    # format variable in the base sentence string. Since it is possible
    # to have multiple variables from the same category, numeric characters,
    # signifying the order of appearance of the object is removed when
    # searching through the corpus
    substitutions = {cat: random.choice(corpus[non_numeric_string(cat)])
                     for cat in FORMAT_STR.finditer(base_sentence)}

    # Double asterisk notation is used to pass a dictionary to the format
    # method.
    return base_sentence.format(**substitutions).replace("  ", " ")
