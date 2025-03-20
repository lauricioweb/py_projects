livros  = {
    "22424":{
        "titulo":"teste1",
        "autor":"laurifio",
        "ano":123
    },
    "53424":{
        "titulo":"teste2",
        "autor":"laur",
        "ano":1123
    }
}

for livro in livros:
    print(livro)
    for key, value in livros[livro].items():
        print(f"{key}: {value}", end="\n")
    print("\n")

# pasasndo tuplas como chave de um dicionario

dicionario = {}
minha_chave = (1,2,3)

dicionario[minha_chave] = "lauricio es muito lindo, nunca havera ninguem que se compare"

print(dicionario)