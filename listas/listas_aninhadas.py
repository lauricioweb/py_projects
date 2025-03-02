# listas aninhadas

matriz = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

# iterando sobre cada linha da matriz

for coluna in matriz:
      for linha in coluna:
            print(linha, end=" ")
      
      print()


print("====================================")

transposta = []

# para loop para cada coluna

for coluna_t in range(len(matriz[0])): #[1,2,4] colunas
      linha_temporaria = []
      print("coluna ", coluna_t)
      for linha_t in range(len(matriz)): # pegando todas as linha
            print("linha", linha_t)
            linha_temporaria.append(matriz[linha_t][coluna_t]) # sera adicionado o item zero de cada linha na primeira volta
      transposta.append(linha_temporaria)


print(transposta)

