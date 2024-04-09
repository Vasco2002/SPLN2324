# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
from spacy import displacy
import jjcli


nlp = spacy.load("pt_core_news_lg")


text = ("""O Roberto e a Roberta foram passear a Viana do Castelo e deixaram a porta aberta. 
        A gata deles, a Alberta, fugiu.
        Tinha um ar muito triste e foi para a praia.""")

doc = nlp(text)

# renderizar o doc com a entidade reconhecida
rend = displacy.render(doc, style="ent", jupyter=False)
# escrever rend para um ficheiro html
with open('test.html', 'w') as file:
    file.write(rend)
    file.write('<hr/>\n') 

    
