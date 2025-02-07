# função lamda com sorted

pessoas = [("lauro",5), ("ketlin",8), ("lorenzo", 4)]
pessoas_ordenandas = sorted(pessoas,key=lambda x: x[1]) 

# o x = a cada tupla dentro do array, então x[1] esta pegando o segundo elemento da tupla

teste = pessoas[1]
print(teste)