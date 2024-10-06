# imprimindo posição de cada letra de uma string;

posicao_Letra = "python"
print(posicao_Letra[0])
print(posicao_Letra[1])
print(posicao_Letra[2])
print(posicao_Letra[3])
print(posicao_Letra[4])
print(posicao_Letra[5])


# print("lauricio es foda demais")

# pegando partes de uma string

frase = "Olá, Mundo!"

parte = frase[4:8]
# o primeiro parametro passado é o indicie apartir de onde sera imprimido
# o segutdo é até onde;
print(parte)


# pegando apenas as 5 priomeiras letras da frase
primeiros = frase[:5]
print("primeiros", primeiros)

# pegando as 6 ultimas letras da frase;

ultimas = frase[-6:]
print(ultimas)

# verificando se existe uma palvra na frase;

frase = "lauricio é o melhor programador"
if "lauricio2" in frase:
    print("sim a palavra esta na frase")


# removendo espaços em branco;

frase = "    mior programador lauricio      "

print("remove espaços em branco de uma frase")

print(frase.strip())
# o strip ira remover da string o caractere informado por parametro
# ex => frase.strip(*)  ira remover todos os "*" da frase


# transformando frase em array separando por espaço em branco;
texto = "este é apenas um texto de exemplo"
texto = texto.split()
print(texto)


# transformando array em frase separadas por espaço em branco

textarr = ["ola", "sou", "apenas", "um", "texto"]
textstr = " ".join(textarr)
print(textstr)


# para inserir variaveis dentro de uma string use "f" antes das aspas da seguinte forma
# f"meu nome é {nome}"


nome = "lauricio"
idade = 33
altura = 1.50

mensagem = f"Olá meu nome é {nome}. e tenho {idade} de idade e minha altura é {altura:.2f} metros"

print(mensagem)


# alterando tamano das letras.

texto = "Olá Mundo!"
textoMaiusculo = texto.upper()
textoMinusculo = texto.lower()
textoCaptalize = texto.capitalize()

print(textoMaiusculo)
print(textoMinusculo)
print(textoCaptalize)


#pegando a quantidade de uma letra que contem na string

ocorrencia = texto.count("o") #ira retornar a quantidade de letra 0 no texto;
print(ocorrencia)

#substituindo caractere
textoSubstituido = texto.replace("Mundo", "Amigo");
print(textoSubstituido)
