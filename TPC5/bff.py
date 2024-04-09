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
    "PRON": "Pronome",
    "CCONJ": "Conjunção",
    "PUNCT": "Pontuação",
    "PROPN": "Nome Próprio"
}

def extract(frase, md):
    doc = nlp(frase)
    bffdic = {}

    # Inicializando o dicionário de contagem de amigos
    for entidade in doc.ents:
        if entidade.label_ == "PROPN":  # Apenas considerando entidades do tipo PROPN (nomes próprios)
            bffdic[entidade.text] = {}

    # Contando os melhores amigos
    for i, token in enumerate(doc):
        if token.ent_type_ == "PROPN":
            for amigo in token.sent.ents:
                if amigo.text != token.text:  # Ignorando a própria pessoa
                    if amigo.text in bffdic[token.text]:
                        bffdic[token.text][amigo.text] += 1
                    else:
                        bffdic[token.text][amigo.text] = 1

    with open(md, "w", encoding="utf-8") as tabela:
        tabela.write("| Indivíduo | Melhor Amigo | Contagem |\n")
        tabela.write("|---------|--------------|---------|\n")
        for pessoa, amigos in bffdic.items():
            tabela.write(f"| {pessoa} | ")
            if amigos:
                melhor_amigo = max(amigos, key=amigos.get)
                tabela.write(f"{melhor_amigo} | {amigos[melhor_amigo]} |\n")
            else:
                tabela.write("Nenhum | 0 |\n")

if len(sys.argv) != 2:
    input = "default.txt"
else:
    input = sys.argv[1]

with open(input, "r", encoding="utf-8") as arquivo_txt:
    frase = arquivo_txt.read().strip().replace('\n', ' ')

extract(frase, "out2.md")

print(f"As informações de '{input}' foram guardadas no out2.md")
