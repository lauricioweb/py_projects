def analytics(*args):

  return max(args), min(args), sum(args) / len(args)

numeros = list(map(float, input("digite numeros separados por espaço").split()))

maior,menor,media = analytics(*numeros)
# o * é usado para desempacotar uma lista de numeros

print(f"maior numero{maior}")
print(f"menor numero{menor}")
print(f"media numero{media}")