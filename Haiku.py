from random import randint

vowels = 'aeouiy'

f = open('words.txt')
lines = f.readlines()

def syllable(word):
    count = 0
    i = 0
    while True:
        if word[i] not in vowels \
                and i != len(word) - 1\
                and (word[i-1] in vowels):
            count += 1
        i += 1

        if len(word) == i:
            break
    return count


def write_line(syl):
    count = 0
    line = ''
    while count != syl:
        word = lines[randint(0, len(lines)-1)]
        if syllable(word) + count <= syl:
            line += word[:-1] + ' '
            count += syllable(word)
    return line


haiku = write_line(5) + '\n' + write_line(7) + '\n' + write_line(5) + '\n'

print(haiku)


import twitter as tw








