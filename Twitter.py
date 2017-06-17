from twython import Twython
from time import sleep
from random import randint


fhandle = open('words.txt')
lines = fhandle.readlines()


tweet_length = 140  # characters
vowels = 'aeouiy'
sleep_time = 600  # seconds

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)


def syllable(word):
    count = 0
    i = 0
    while True:
        if word[i] not in vowels \
                and i != len(word) - 1\
                and (word[i - 1] in vowels):
            count += 1
        i += 1

        if len(word) == i:
            break
    return count


def write_line(syl):
    count = 0
    line = ''
    while count != syl:
        word = random.choice(lines)
        if syllable(word) + count <= syl:
            line += word[:-1] + ' '
            count += syllable(word)
    return line


def write_haiku():
    haiku = "{}\n{}\n{}".format(write_line(5),
                                write_line(7),
                                write_line(5))
    haiku = haiku[:-1].capitalize() + "."
    return haiku


def post_haiku(haiku):
    twitter.update_status(status=haiku)

a = write_haiku()
print(a)

if __name__ == "__main__":
    count = 0
    while True:
        if count < 24:
            post_haiku(write_haiku())
            count += 1
            sleep(3600)
        else:
            break
