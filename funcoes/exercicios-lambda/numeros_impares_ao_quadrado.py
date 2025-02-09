"""
converta uma lista de numeros para uma nova lista pegando apenas os numero impares
depois crie uma nova lista transformando esses numeros ao quadrado

"""

lista = [1,2,3,4,66,43,42,31,34,441]

numbers_unpar = list(filter(lambda number: number % 2 != 0, lista))

numbers_upper = list(map(lambda number: number ** 2, numbers_unpar))

print("numeros impares \n")
print(numbers_unpar)

print("numeros impares ao quadrado \n")
print(numbers_upper)

