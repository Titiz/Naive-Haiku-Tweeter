from random import randint

verbs = open('verbs.txt')
verbs = verbs.readlines()
vl = len(verbs) - 1

nouns = open('nouns.txt')
nouns = nouns.readlines()
nl = len(nouns) - 1

adverbs = open('adverbs.txt')
adverbs = adverbs.readlines()
advl = len(adverbs) -1

adjectives = open('adjectives.txt')
adjectives = adjectives.readlines()
adjl = len(adjectives) - 1

prepositions = open('prepositions.txt')
prepositions = prepositions.readlines()
pl = len(prepositions) - 1

junctions = ['and ', 'or ', ', but ', ', yet ', 'then ']
jl = len(junctions) - 1

articles = ['a ', 'the ', '']
arl = len(articles) - 1


def write_sentence(n):
    if n == 0:      # I went to the park
        n_1 = nouns[randint(0, nl)][:-1]
        v_1 = verbs[randint(0, vl)][:-1]
        p_1 = prepositions[randint(0, pl)][:-1]
        a_1 = articles[randint(0, arl)][:-1]
        n_2 = nouns[randint(0, nl)][:-1]
        return n_1 + ' ' + v_1 + ' ' + p_1 + ' ' + a_1 + ' ' + n_2
    if n == 1:      #Hot like the sun (simile)
        adj_1 = adjectives[randint(0, adjl)][:-1]
        a_1 = articles[randint(0, arl)][:-1]
        n_1 = nouns[randint(0, nl)][:-1]
        return adj_1 + ' like ' + 'the' + ' ' + n_1
    if n == 2:          #jayden
        n_1 = nouns[randint(0, nl)][:-1]
        n_2 = nouns[randint(0, nl)][:-1]
        v_1 = verbs[randint(0, vl)][:-1]
        v_2 = verbs[randint(0, vl)][:-1]
        j_1 = junctions[randint(0, jl)][:-1]
        return 'if ' + n_1 + ' ' + v_1 + ' ' + 'then' + ' how ' + n_2 + ' ' + v_2
print(write_sentence(2))
