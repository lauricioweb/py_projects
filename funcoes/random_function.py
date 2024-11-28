import random
# são numeros randomicos - numeros aleatorios entre um numero e outro.
print(random.randrange(1, 30))
# retorna de um numero inicial a um numero final
print(random.random())  # retorna um numero um numero quebrado.
print(random.randint(1, 54))
# retorna numero inteiro aleatorio entre dois numero


# escolhendo aleatoriamente um elemento da lista;
frutas = ["maça", "cereja", "banana"]
print(random.choice(frutas))

# embaralhando aleatoiramente uma lista;
numeros = [2, 65, 12, 22, 124, 45, 11]
random.shuffle(numeros)  # lista esta embaralhada
print(numeros)

# gerando numeros flutuantes em um intervalo definido

print(random.uniform(3.1, 3.6))
