import requests
from lxml import html
import requests
import json
import logging  # TODO Start using logging

from tqdm import tqdm


def build_corpus() -> dict:
    """Using an initial word list, identify the parts of speech, and then store
    the corpus in JSON for ease of access."""
    with open('words.txt') as fhandle:
        lines = [line.strip() for line in fhandle.readlines()]

    # Listing of the words, and whether they are nouns, adjectives, etc
    word_type = {}

    # TODO Figure out if there's a quicker way of handling the website
    # download, as currently, it's not cutting it
    # TODO Handle exceptions
    for word in tqdm(lines):
        try:
            page = requests.get(
                'http://dictionary.reference.com/browse/' + word)
            tree = html.fromstring(page.content)
        except Exception as e:
            print(e)
        # The element containing the language category of the given word
        # should always come first on the page, though this could change
        # if the website is reworked
        try:
            lang_part = tree.xpath('//span[@class="dbox-pg"]')[0]
            word_type[word] = lang_part.text
        except IndexError as e:
            pass

    # Taking the parts of speech and making them into dictionary keys
    headers = set(word_type.values())
    generated_corpus = {header: [] for header in list(headers)}
    additional_corpus = {'articles': ['a', 'the', ''],
                         'junctions': ['and', 'or', ', but', ', yet', 'then']
                         }
    corpus = {**generated_corpus, **additional_corpus}

    # Reversing the dictionary
    for key, value in lang_part.items():
        corpus[value].append(key)

    # Saves the result as a JSON file for later usage (removes need for
    # individual text files)
    json.dump(corpus, open("corpus.json", 'w+'), sort_keys=True, indent=4)

    return corpus


def load_corpus() -> dict:
    """Load corpus from JSON file."""
    corpus = json.load(open("corpus.json"))
    return corpus
