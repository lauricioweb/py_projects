num =  int(input("digite um numero"))
soma = 0
acumulador = 0

for i in range(1, num + 1):
  print(f"{i} * {i} = {i * i}")
  soma = i * i
  acumulador += soma


print(f"acumulador {acumulador}")
