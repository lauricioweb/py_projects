
produtos = {
    "mouse":200,
    "notebook":1300,
    "pendrive":300,
    "monitor":4000
}

mais_caros = {}

mais_baratos = {chave: valor for chave, valor in produtos.items() if valor < 500}

print(mais_baratos)


for produto, preco in produtos.items():
    if preco > 300 : mais_caros[produto] = preco

print(mais_caros)


