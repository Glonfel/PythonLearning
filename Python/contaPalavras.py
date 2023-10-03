import string
from collections import Counter

def processar_texto(text):
    tradutor = str.maketrans('', '', string.punctuation) #Remove pontuações
    text = text.translate(tradutor).lower() #Converte para lowercase
    palavras= text.split()
    return palavras

def rank_palavras(arquivo, n):
    with open(arquivo, 'r') as file:
        text = file.read()

    palavras = processar_texto(text)
    conta_palavras = Counter(palavras)
    comuns = conta_palavras.most_common(n)

    print(f"As {n} Palavras mais comuns: \n")
    for p, c in comuns:
        print(f"{p}: {c}")

arquivo = 'teste.txt'
n = 7
rank_palavras(arquivo, n)