"""

operaçoes basicas
 - adicionar: append(), insert()
 - remover: remove(), pop()
 - concatenar: +, extend()
 - repetir: *
 - verificar se um item esta na lista: in
 - sort(): ordena a lista in-place
 - reverse(): inverte a ordem dos elemntos in-place
 - count(): conta o numero de ocorrencias de um elemento na lista
 - index(): retorna o indice da primeira ocorrencia de um elemnto

"""

# adicionando

# append adiciona o novo item como ultimo
frutas = ["uva","abacate","morango"]
frutas.append("pera")

print(frutas)

# insert adiona o item em uma posição especificada 

frutas.insert(1,"melancia")
print(frutas)

#removendo

# remove() remove  o primeiro item que for igual ao valor especificado
frutas.remove("uva")
print(frutas)

# pop() remove o item no indice especificado
frutas.pop(1) # remove o ultimo item se nao for passado nenhum parametro
#retorna o animal removido
print(frutas)

print("=========================================")
#--- concatenando listas

# + une duas listas

lista1 = [1,2,3]
lista2 = [5,4,2]

lista3 = lista1 + lista2
print(lista3)

# extend recebe uma lista na qual sera extendida
# este motodo modifica a lista original

lista1.extend(lista2)
print(lista1)


print("============================")

# repeticao de listas
repeticao = [1,2,3,4] * 5
print(repeticao)


# verificando items da lista
items = ["casa","carro","apartamento"]

print("casa" in items)


print("=============================")

# sort() ordena os items de uma lista em ordem crescente para numeros e alfabeticapara strings

lista_de_frutas = ["pera","maca","banana","banana","morango", "uva"]
lista_de_numeros = [1,2,45,4,5]

lista_de_frutas.sort()
print(lista_de_frutas)

lista_de_numeros.sort() # para ordenar na forma decrecente use reverse=True 
print(lista_de_numeros)

print("====================")

# reverse() reverte a ordem dos elementos da lista (esta funcao nao retorna a lista reversa  apenas modifica a lista na qual foi chamada esta metodo)

normal_list = ["maca","morango","uva","melancia"]
normal_list.reverse()
print(normal_list)

print("====================")


# count() retorna o numero de vezes que um elemento aparece na lista

lista_nomes = ["lauricio","mariana","luiza","yasmin", "yasmin","yasmin"]

quantidade_elemento = lista_nomes.count("yasmin")
print(quantidade_elemento)