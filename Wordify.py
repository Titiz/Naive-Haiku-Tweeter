import requests
import lxml.html as lh
import json

with open('words.txt') as fhandle:
    lines = [line.strip() for line in fhandle.readlines()]

# Listing of the words, and whether they are nouns, adjectives, etc
word_type = {}
s = open('wordsl.txt', 'a')

for word in lines:
    page = lh.parse('http://dictionary.reference.com/browse/' + word)

    # The element containing the language category of the given word
    # should always come first on the page, though this could change
    # if the website is reworked
    lang_part = page.xpath('//span[@class="dbox-pg"]')[0]
    word_type[word] = lang_part.text

    # TODO Invert dictionary - remove word files and access 
