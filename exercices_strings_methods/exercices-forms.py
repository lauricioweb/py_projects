altura = 3
largura = 13

for l in range(altura):
  
  for c in range(largura):
    print("*", end=" ")

  print()


print("--------------------")

print("triangulo")

alturaTri = 5
for i in range(alturaTri):
  espacos = alturaTri - i -1
  asteriscos = 2 * i + 1
  print(" " * espacos + "*" * asteriscos) 