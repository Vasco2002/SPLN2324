import spacy
import sys

nlp = spacy.load("pt_core_news_lg")

expansion = {
    "DET": "Determinante",
    "NOUN": "Nome",
    "AUX": "Auxiliar",
    "VERB": "Verbo",
    "ADV": "Advérbio",
    "ADP": "Preposição",
    "PUNCT": "Pontuação"
}

def extract(frase, md):
    doc = nlp(frase)
    with open(md, "w", encoding="utf-8") as tabela:
        tabela.write("| Palavra | Tipo | Lema |\n")
        tabela.write("|---------|------|------|\n")
        for token in doc:
            tipo = expansion.get(token.pos_, token.pos_)
            tabela.write(f"| {token.text} | {tipo} | {token.lemma_} |\n")

if len(sys.argv) != 2:
    input = "default.txt"
else:
    input = sys.argv[1]

with open(input, "r", encoding="utf-8") as arquivo_txt:
    frase = arquivo_txt.read().strip().replace('\n', ' ')

extract(frase, "out.md")

print(f"Informações de '{input}' foram guardadas no out.md")
