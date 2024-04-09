import spacy
from collections import Counter
import sys

with open(sys.argv[1]) as file:
    content = file.read()

nlp = spacy.load("pt_core_news_lg")

doc = nlp(content)

voc = nlp.vocab

verbos = Counter()

for sentence in doc.sents:
    for token in sentence:
        if token.pos_ == "VERB":
            verbos[token.lemma_] += 1

#print(verbos.most_common(20))
verbo_normalizado = Counter()

for verbo, ocorr in verbos.most_common(1000):
    rank = voc[verbo].rank
    verbo_normalizado[verbo] = ocorr * (rank + 2.6)
    frequencia = 1 / (rank + 2.6)
    print(verbo, ocorr, rank)