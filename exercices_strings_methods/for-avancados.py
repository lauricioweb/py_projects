# Nested loops = aninhar um ou mais loops dentro de outro

for i in range(1, 4):
    for j in range(1, 4):
        #print(i, "*", j, "=", i * j)
        pass

# Imprimindo quadrados ímpares
quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
#print(quadrados_impares)

# Alternativa com loop for:
quadrados_impares = []
for x in range(10):
    if x % 2 != 0:
        quadrados_impares.append(x**2)
#print(quadrados_impares)

# Imprimindo consoantes
palavra = "programacao"
consoantes = [letra for letra in palavra if letra not in "aeiou"]
#print(consoantes)

# Alternativa com loop for:
consoantes = []
for letra in palavra:
    if letra not in "aeiou":
        consoantes.append(letra)
#print(consoantes)

#list compressed
texto = "helloword"
consoantes = [char for char in texto if char.lower() not in "aeiou"]
print(consoantes)
