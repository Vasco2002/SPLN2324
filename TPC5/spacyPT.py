import spacy
import sys
from spacy import displacy

nlp = spacy.load("pt_core_news_lg")

expansion = {
    "DET": "Determinante",
    "NOUN": "Nome",
    "AUX": "Auxiliar",
    "VERB": "Verbo",
    "ADV": "Advérbio",
    "ADP": "Preposição",
    "PRON": "Pronome",
    "CCONJ": "Conjunção",
    "PUNCT": "Pontuação",
}

def extract(frase, md):
    doc = nlp(frase)
    with open(md, "w", encoding="utf-8") as tabela:
        tabela.write("| Palavra | Tipo | Lema | Dep | Filhos |\n")
        tabela.write("|---------|------|------|-----|--------|\n")
        for i, token in enumerate(doc):
            if token.is_space:
                continue
            tipo = expansion.get(token.pos_, token.pos_)
            filhos = ", ".join([child.text for child in token.children])
            tabela.write(f"| {token.text} | {tipo} | {token.lemma_} | {token.dep_} | {filhos} |\n")
            if token.is_sent_end:
                tabela.write("|         |      |      |     |         |\n")
#    displacy.serve(doc, style="dep")

if len(sys.argv) != 2:
    input = "default.txt"
else:
    input = sys.argv[1]

with open(input, "r", encoding="utf-8") as arquivo_txt:
    frase = arquivo_txt.read().strip().replace('\n', ' ')

extract(frase, "out.md")

print(f"As informações de '{input}' foram guardadas no out.md")
