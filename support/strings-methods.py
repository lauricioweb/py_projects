# Criando uma string
texto = "Python é incrível!"

# 1. upper() - Converte todos os caracteres para maiúsculas
print("1. upper():", texto.upper())  # "PYTHON É INCRÍVEL!"

# 2. lower() - Converte todos os caracteres para minúsculas
print("2. lower():", texto.lower())  # "python é incrível!"

# 3. capitalize() - Coloca a primeira letra em maiúscula
print("3. capitalize():", texto.capitalize())  # "Python é incrível!"

# 4. title() - Coloca a primeira letra de cada palavra em maiúscula
print("4. title():", texto.title())  # "Python É Incrível!"

# 5. strip() - Remove espaços em branco no início e no final
espacos = "   espaço extra   "
print("5. strip():", espacos.strip())  # "espaço extra"

# 6. lstrip() - Remove espaços em branco no início
print("6. lstrip():", espacos.lstrip())  # "espaço extra   "

# 7. rstrip() - Remove espaços em branco no final
print("7. rstrip():", espacos.rstrip())  # "   espaço extra"

# 8. replace() - Substitui partes da string
print("8. replace():", texto.replace("incrível", "fantástico"))  # "Python é fantástico!"

# 9. split() - Divide a string em uma lista usando um separador
print("9. split():", texto.split())  # ['Python', 'é', 'incrível!']

# 10. join() - Junta elementos de uma lista em uma única string
lista = ["Python", "é", "fantástico"]
print("10. join():", " ".join(lista))  # "Python é fantástico"

# 11. find() - Retorna o índice da primeira ocorrência de um valor
print("11. find('é'):", texto.find("é"))  # 7

# 12. rfind() - Retorna o índice da última ocorrência de um valor
texto_reverso = "Python é incrível e único!"
print("12. rfind('é'):", texto_reverso.rfind("é"))  # 18

# 13. startswith() - Verifica se a string começa com um valor específico
print("13. startswith('Python'):", texto.startswith("Python"))  # True

# 14. endswith() - Verifica se a string termina com um valor específico
print("14. endswith('!'):", texto.endswith("!"))  # True

# 15. isalpha() - Verifica se todos os caracteres são letras
apenas_letras = "Python"
print("15. isalpha('Python'):", apenas_letras.isalpha())  # True

# 16. isdigit() - Verifica se todos os caracteres são números
apenas_numeros = "12345"
print("16. isdigit('12345'):", apenas_numeros.isdigit())  # True

# 17. isnumeric() - Similar a isdigit(), mas considera números como frações
fracao = "½"
print("17. isnumeric('½'):", fracao.isnumeric())  # True

# 18. isalnum() - Verifica se todos os caracteres são alfanuméricos
mistura = "Python3"
print("18. isalnum('Python3'):", mistura.isalnum())  # True

# 19. count() - Conta quantas vezes um valor aparece na string
print("19. count('é'):", texto.count("é"))  # 1

# 20. center() - Centraliza a string em um espaço de largura específica
print("20. center(30):", texto.center(30, "-"))  # "---Python é incrível!---"

# 21. zfill() - Preenche a string com zeros à esquerda até atingir um comprimento
numero = "42"
print("21. zfill(5):", numero.zfill(5))  # "00042"

# 22. casefold() - Similar a lower(), mas mais agressivo (útil para comparações)
maiuscula = "MAIÚSCULA"
print("22. casefold():", maiuscula.casefold())  # "maiúscula"
