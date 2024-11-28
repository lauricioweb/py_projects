n = 10  # Altere esse valor para calcular a soma de diferentes quantidades de números ímpares

contador = 0
soma = 0
numero_impar_atual = 1

# Loop para somar os primeiros n números ímpares
while contador < n:
    soma += numero_impar_atual  
    numero_impar_atual += 2     
    contador += 1               

# Exibe o resultado final
print(f"A soma dos primeiros {n} números ímpares é: {soma}")
