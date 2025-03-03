
# usando enumerate para iterar obtendo o indice e o valor de itens

lista = ["maca","uva","morango","melancia","banana"]

for index, fruta in enumerate(lista):
    print(f"o indice {index} e o valor {fruta}")


notas = [12,34,34,22,12]
alunos = ["maeria","joana","antonia","raimunda","francisca"]

for index, aluno in enumerate(alunos):
    print(f"indice {index} aluno: {aluno}")
    print(f"a nota do aluno {aluno} é {notas[index]}")


# fazendo com tuplas 
print("========================")
alunos2 = [("mariana",22),("rafaela",44),("clara",21)]

for index, aluno in  enumerate(alunos2):
    print(f"id: {index} \n nome: {aluno[0]} \n nota: {aluno[1]} \n")