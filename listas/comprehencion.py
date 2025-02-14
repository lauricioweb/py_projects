"""
list comprehensios 
   uma maneira de criar listas: [x**2 for x in range(10) if x % 2 == 0]

   list comprehensions sao uma das caracteristicas mais utei e elegantes de python.

   elas oferecem uma maneira de criar listas, e sao frequentemente mais compreensiveis e  mais eficientes do que usar loops

   nova_lista = [expressão for item in iterável]

  
"""

quadrados = [x**2 for x in range(10)]
print(quadrados)

nomes = ["maria","ana","julio","alie","alice"]
adicionando = [x.upper() for x in nomes if x[0] == "a"]
#retornara a nova lista apenas o nomes que comecam com a letra a
print(adicionando)
