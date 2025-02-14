# slice é o metodo usado para fatiar listas

# acessando subconjuntos em uma lista
# trata-se de acessar apenas uma parte especifica da lista que pode ser especificada informando o indice do elemento inicila e do elemento final;

exemplo_lista = [0,1,2,3,4,5,6]

subconjunto = exemplo_lista[1:4] #acessando apenas do indice 1 a 4
print(subconjunto)

# se omitir o indice inicial, o python ira pegar o indice inicial
final = exemplo_lista[:3] # saida [0,1,2]
print(final)

# se omitir o indice final o python  ira pegar partir do primeiro idice ate o final

inicial = exemplo_lista[4:] # saida [4,5,6]
print(inicial)

# obtendo indices alternadamente usando [::2] isso indica que ele ira pegar um elemento e ignorar o outro

alternados = exemplo_lista[::2] #saida [0,2,4,6]
print(alternados)

# definindo o limite para o acesso auternado

alternado_limited = exemplo_lista[1:5:2]
print(alternado_limited)