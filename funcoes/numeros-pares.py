numero = 0

max = int(input("Digite um numero maior que 1"))

print("numeros pares de ", numero, " até ", max)

while numero <= max:
    
    if numero % 2 == 0:
        print(numero, end=" ")
    
    numero += 1

