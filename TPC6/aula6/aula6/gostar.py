# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
from spacy import displacy
from spacy.matcher import Matcher, DependencyMatcher
from jjcli import *


nlp = spacy.load("pt_core_news_lg")
matcher = Matcher(nlp.vocab)

# pattern: gostava de/do + verbo
pattern = [
    {"LEMMA": "gostar"},
    {"LOWER": {"IN": ["de", "do", "da"]}},
    {"OP": "?"}, # optional
    {"POS": "VERB"}
]
matcher.add("Gostar de", [pattern])

""" text = ('''O Roberto e a Roberta foram passear a Viana do Castelo e deixaram a porta aberta. 
        A gata deles, a Alberta, fugiu.
        Foi fundado um monumento em honra a isso.
        Gostava de cantar.''') """

# open file HP.txt and use it as input
with open("HP.txt", "r") as f:
     text = f.read()


doc = nlp(text)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[end - 1]
    print("Match found:", string_id, span.text)


