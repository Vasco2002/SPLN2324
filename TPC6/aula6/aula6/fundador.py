# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
from spacy import displacy
from spacy.matcher import Matcher, DependencyMatcher
from jjcli import *


nlp = spacy.load("pt_core_news_lg")
matcher = DependencyMatcher(nlp.vocab)



pattern = [
    # anchor token: founded
    {
        "RIGHT_ID": "fundar",
        "RIGHT_ATTRS": {"LEMMA": "fundar"}
    },
    # founded -> subject
    {
        "LEFT_ID": "fundar",
        "REL_OP": ">",
        "RIGHT_ID": "subject",
        "RIGHT_ATTRS": {"DEP": "nsubj"}
    },
    # 'founded' follows 'initially'
    {
        "LEFT_ID": "fundar",
        "REL_OP": ">",
        "RIGHT_ID": "objeto",
        "RIGHT_ATTRS": {"DEP": "obj"}
    }
]

matcher.add("Fundador de", [pattern])

pattern = [
    # anchor token: founded
    {
        "RIGHT_ID": "fundar",
        "RIGHT_ATTRS": {"LEMMA": "fundar"}
    },
    # founded -> subject
    {
        "LEFT_ID": "fundar",
        "REL_OP": ">",
        "RIGHT_ID": "subject",
        "RIGHT_ATTRS": {"DEP": "obl:agent"}
    },
    # 'founded' follows 'initially'
    {
        "LEFT_ID": "fundar",
        "REL_OP": ">",
        "RIGHT_ID": "objeto",
        "RIGHT_ATTRS": {"DEP": "nsubj:pass"}
    }
]

matcher.add("Fundado por", [pattern])

text = ('''O Roberto e a Roberta foram passear a Viana do Castelo e deixaram a porta aberta. 
        A gata deles, a Alberta, fugiu.
        Foi fundado um monumento em honra a isso.
        Gostava de cantar.
        O Roberto fundou a empresa em 1999.''')

# open file HP.txt and use it as input
""" with open("HP.txt", "r") as f:
     text = f.read() """


doc = nlp(text)

# retokenize 
with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)

matches = matcher(doc)
if matches:
    for match_id, match in matches:
        string_id = nlp.vocab.strings[match_id]
        print("Match found:", string_id, doc[match[0]], doc[match[1]], doc[match[2]])
else:
    print("No match found.")