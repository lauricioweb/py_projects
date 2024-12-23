from array import array

# Criando um array de inteiros
numeros = array('i', [1, 2, 3, 4, 5])  # 'i' representa inteiros

# Métodos do array
# append()
numeros.append(6)
print("Após append(6):", numeros.tolist())  # [1, 2, 3, 4, 5, 6]

# extend()
numeros.extend([7, 8, 9])
print("Após extend([7, 8, 9]):", numeros.tolist())  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert()
numeros.insert(3, 99)  # Insere 99 na posição 3
print("Após insert(3, 99):", numeros.tolist())  # [1, 2, 3, 99, 4, 5, 6, 7, 8, 9]

# pop()
removido = numeros.pop(3)  # Remove o elemento da posição 3
print("Após pop(3):", numeros.tolist())  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Elemento removido:", removido)  # 99

# reverse()
numeros.reverse()
print("Após reverse():", numeros.tolist())  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

""" Resumo dos métodos mais usados:
Método	Descrição
append()	Adiciona um item ao final da lista.
extend()	Adiciona vários itens ao final da lista.
insert()	Insere um item em uma posição específica.
remove()	Remove a primeira ocorrência de um valor.
pop()	Remove e retorna um item por índice (ou o último).
index()	Retorna o índice de um item na lista.
count()	Conta quantas vezes um valor aparece na lista.
sort()	Ordena a lista em ordem crescente (ou personalizada).
reverse()	Inverte a ordem dos itens na lista.
copy()	Retorna uma cópia da lista.
clear()	Remove todos os itens da lista. """

