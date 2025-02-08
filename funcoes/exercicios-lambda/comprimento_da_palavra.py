"""
crie uma funcao que recebe uma lista de palavras e retorne uma nova lista contendo o cumprimento
de cada palavras

"""

lista = ["casa","carro","apartamento"]

length_words = list(map(lambda word: len(word),lista))

print(length_words)

