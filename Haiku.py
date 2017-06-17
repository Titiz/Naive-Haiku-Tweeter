import random

import twitter as tw

VOWELS = 'aeouiy'

with open('words.txt') as fhandle:
    lines = [word.strip() for word in fhandle.readlines()]


def syllable(word: str) -> int:
    count = 0
    for ind, char in enumerate(word):
        if char not in VOWELS and word[ind - 1] in VOWELS:
            count += 1
    return count


def write_line(syl):
    line = ''
    while syllable(line) < syl:
        word = random.choice(lines)
        if syllable(word) + syllable(line) <= syl:
            line += word + " "
    return line.strip()


def write_haiku():
    haiku = "{}\n{}\n{}.".format(write_line(5),
                                 write_line(7),
                                 write_line(5))
    return haiku.strip().capitalize()

if __name__ == '__main__':
    print(write_haiku())
