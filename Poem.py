import random
import re

# Precompilation of the regex so that it would not have to be compiled
# every iteration, saving time overall
FORMAT_STR = re.compile("{(.*?)}")

# Possible sentence constructions. As we go along, can add many more
# and then divide them into beginning, body and end constructions,
# allowing for a wider variety of sentences.
SENTENCES = [
    "{nouns1} {verbs} {prepositions} {articles} {nouns2}",
    "{adjectives} like the {nouns}",
    "if {nouns1} {verbs1} then how {nouns2} {verbs2}"
]

corpus = {'articles': ['a', 'the', ''],
          'junctions': ['and', 'or', ', but', ', yet', 'then']
          }

# Removing objects from the global namespace once the module is imported
_files = ['verbs.txt', 'nouns.txt', 'adverbs.txt',
          'adjectives.txt', 'prepositions.txt']

for file in _files:
    with open(file) as fhandle:
        corpus[file.split(".")[0]] = [line.strip()
                                      for line in fhandle.readlines()]


def non_numeric_string(string: str) -> str:
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
