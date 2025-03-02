matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#localziando numero 6
print(matriz[1][2])

soma = 0
for linha in matriz:
    for numero in linha:
        soma += numero
print(soma)

print("exercicio 3")

for coluna_t in matriz:

    for linha_t in coluna_t:
        print(linha_t, end="\t")
    print()