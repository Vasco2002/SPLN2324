#!/usr/bin/env python3

'''
Name 
    WordOccur - Calculates words Occurenceis in a text

SYNOPSIS
    WordOccur [options] input_files
    option: 
        -m 20 - Show the 20 most common
        -n: Order alfabetically
        -l: join lower case with upper case

DESCRIPTIONS

'''

from collections import Counter
from jjcli import *
import re

__version__ = "0.0.1"

def tokeniza(text):
    palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:?!_—]+', text)
    # ?: agrupa regex, mas não são tratadas como grupo de captura
    return palavras

def printWordsList(list):
    for word, numb in list:
        print(f"{numb}  {word}")

def main():

    cl = clfilter("nlm:", doc=__doc__) ## Option values in cl.opt dictionary

    for txt in cl.text():   
        if "-l" in cl.opt:     ## Process one file at time
            wordsList = tokeniza(txt.lower())
        else:
            wordsList = tokeniza(txt) 

        if "-n" in cl.opt:
            wordsList.sort()
    
        if "-m" in cl.opt:
            c = Counter(wordsList)
            printWordsList(c.most_common(int(cl.opt.get("-m"))))
        else:
            c = Counter(wordsList)
            printWordsList(c.items())


# chmod 755 filename, transforma o código num script