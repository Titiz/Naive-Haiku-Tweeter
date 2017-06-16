import random

import twitter as tw

VOWELS = 'aeouiy'

with open('words.txt') as fhandle:
    lines = fhandle.readlines()


def syllable(word: str) -> int:
    count = 0
    for ind, char in enumerate(word):
        if char not in VOWELS and word[ind - 1] in VOWELS:
            count += 1
    return count


def write_line(syl):
    count = 0
    line = ''
    while count != syl:
        word = random.choice(lines)
        if syllable(word) + count <= syl:
            line += word[:-1] + " "
            count += syllable(word)
    return line


haiku = write_line(5) + '\n' + write_line(7) + '\n' + write_line(5) + '\n'

print(haiku)
