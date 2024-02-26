#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates the word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Shows the 20 most frequent words
        -n : Order alfabetically
        -n + -m 20 : Shows the 20 first words in alfabetic order
   
Description'''

from jjcli import * 
from collections import Counter
import sys
import re

cl=clfilter("nm:", doc=__doc__)

def tokaniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[.,?!;:—]+', texto)
    return palavras

def imprime(lista, alfabetic):
    if alfabetic == 1:
        print(f"Palavra --> Nº de Ocorrência")
    else:
        print(f"Nº de Ocorrência --> Palavra") 
    for palavra, n_ocorr in lista:
        if alfabetic == 1:
            print(f"{palavra} --> {n_ocorr}")
        else:
            print(f"{n_ocorr} --> {palavra}") 
        
for txt in cl.text():
    lista_palavras = tokaniza(txt)
    ocorr = Counter(lista_palavras).items()
    alfabetic = 0
    if "-n" in cl.opt:
            ocorr = sorted(ocorr, key=lambda x: x[0])
            alfabetic = 1
    if "-m" in cl.opt:
        if alfabetic == 0:
            ocorr = sorted(ocorr, key=lambda x: x[1], reverse=True)
        ocorr = ocorr[:int(cl.opt.get("-m"))]
    imprime(ocorr, alfabetic)



