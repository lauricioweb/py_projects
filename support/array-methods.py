# Criando uma lista
numeros = [10, 20, 30, 40, 50]

# 1. append() - Adiciona um elemento ao final da lista
numeros.append(60)
print("Após append(60):", numeros)  # [10, 20, 30, 40, 50, 60]

# 2. extend() - Adiciona múltiplos elementos ao final
numeros.extend([70, 80])
print("Após extend([70, 80]):", numeros)  # [10, 20, 30, 40, 50, 60, 70, 80]

# 3. insert() - Insere um elemento em uma posição específica
numeros.insert(2, 25)  # Insere 25 na posição 2
print("Após insert(2, 25):", numeros)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# 4. remove() - Remove a primeira ocorrência de um valor
numeros.remove(30)
print("Após remove(30):", numeros)  # [10, 20, 25, 40, 50, 60, 70, 80]

# 5. pop() - Remove e retorna o elemento de uma posição específica
ultimo = numeros.pop()  # Remove o último elemento
print("Após pop():", numeros)  # [10, 20, 25, 40, 50, 60, 70]
print("Elemento removido pelo pop():", ultimo)  # 80

# 6. index() - Retorna o índice da primeira ocorrência de um valor
indice = numeros.index(50)
print("Índice do número 50:", indice)  # 4

# 7. count() - Conta quantas vezes um valor aparece
contagem = numeros.count(25)
print("Contagem do número 25:", contagem)  # 1

# 8. sort() - Ordena a lista em ordem crescente
numeros.sort()
print("Após sort():", numeros)  # [10, 20, 25, 40, 50, 60, 70]

# 9. reverse() - Inverte a ordem dos elementos
numeros.reverse()
print("Após reverse():", numeros)  # [70, 60, 50, 40, 25, 20, 10]

# 10. copy() - Cria uma cópia rasa da lista
copia = numeros.copy()
print("Cópia da lista:", copia)  # [70, 60, 50, 40, 25, 20, 10]

# 11. clear() - Remove todos os elementos da lista
numeros.clear()
print("Após clear():", numeros)  # []
