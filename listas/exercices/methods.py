"""
cria uma lista chamada numeros contendo os valores: [22,33,21,556,32,41,12,01,23].

ordene a lista em ordem crescente usando o metodo sort() e imprima o resultado

ordene a lista em ordem crescente e imprima o resultado

inverta a lista usando reverse()

conte quantas vezes o numero 32 aparece na lista usando o metodo count() e imprima o resultado 

encontre o indice primeira ocorrencia do numero 32 usando o methodo index() e imprima o resultado

tente encontrar o indice de um numero que nao esta na lista e capture a execulsao usando bloco try execpt para exibir uma mensagem amigavel.

"""


lista_numeros = [22,32,32,32,44,312,21,55,64,12,1]

lista_numeros.sort()
print("ordem crescente")
print(lista_numeros)

lista_numeros.reverse()
print("ordem reversa")
print(lista_numeros)

quantidade_do_elemento = lista_numeros.count(32)
print("quantidade do numero 32 na lista")
print(quantidade_do_elemento)

indicie_numero = lista_numeros.index(32)
print("indice da primeira ocorrencia do numero 32 na lista")
print(indicie_numero)

print("\n")
print("tentando encontrar indice de um elemento que nao esta na lista")

try:

  indice_inexistente = lista_numeros.index(44)
  print(indice_inexistente)
except:
  print("nao xiste elemento neste indice")