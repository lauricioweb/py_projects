n = int(input("digite um numero"))
soma = 0
acumulador = 0

for i in range(1,n + 1):
   if i % 2 == 0:
    print(f"soma {soma} + {i} = {soma + i}")
    soma += i