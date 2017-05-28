import requests




f = open('words.txt')
lines = f.readlines()
dic = {}
s = open('wordsl.txt', 'a')

for word in lines:
    while True:
        try:
            url = 'http://dictionary.reference.com/browse/' + word[:-1]
            headers = {'Accept-Encoding': 'identity'}
            f = requests.get(url)
            f_text = f.text.lower()
            i = 0
            diff = 10000
            break
        except requests.exceptions.ConnectionError:
            pass
    while True:
        e = ''
        write = True
        text = f_text[i: i+diff]
        a = text.count('<span class="dbox-pg">noun')
        b = text.count('<span class="dbox-pg">adjective')
        c = text.count('<span class="dbox-pg">adverb')
        d = text.count('<span class="dbox-pg">preposition')
        f = text.count('<span class="dbox-pg">verb')
        if a > 0:
            e = 'noun'
            break
        if b > 0:
            e = 'adjective'
            break
        if c > 0:
            e = 'adverb'
            break
        if d > 0:
            e = 'preposition'
            break
        if f > 0:
            e = 'verb'
            break
        if text == '':
            print(word)
            write = False
            break
        if i <= 25000:
            i += 5000
            diff = 10000
        else:
            i += 200
            diff = 100
    if write:
        dic[word[:-1]] = e
        s.write(word[:-1] + ',' + e + '\n')
        print(word[:-1], e)
