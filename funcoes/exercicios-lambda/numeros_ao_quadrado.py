"""
crie uma funcao lambda que receba uma lista de numeros e retorne uma nova lista
com esses numeros ao quadrado

"""

lista = [1,2,3,4,5,6]


lista_ao_quadrado = list(map(lambda x : x ** 2, lista))

print(lista_ao_quadrado)

