


def resumo_vendas(produto_1, produto_2):
    total_vendas = produto_1 + produto_2
    mais_vendido = "produto_1 main vendido" if produto_1 > produto_2 else "produto_2 mais vendido"
    return total_vendas,mais_vendido


print(resumo_vendas(239,213))

print("----------------------")

vendas_semana = [(234,211),(123,212),(432,44),(321,362)]

for prod_1, prod_2 in vendas_semana:
    print(f"prod_1 {prod_1} \n prod_2 {prod_2}")

