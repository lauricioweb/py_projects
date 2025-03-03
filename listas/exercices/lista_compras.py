
lista_compras = []

while True:
    response = int(input("1- adicionar item \n 2- remover item \n 3- exibir lista \n 4- sair \n: "))

    if response == 1:
        item = str(input("escreva os items a serem adicionados separado por vigula "))
        itens = item.split(",")
        for my_itens in itens:
            lista_compras.append(my_itens.strip())
        print(lista_compras)
    elif response == 2:
        item = str(input("escrava o nome do item que deve ser removido \n para remover mais de um item escreva separando po virgula "))
        itens_removed = item.split(",")
        print(itens_removed)
        for itens in itens_removed:
            itens_clean = itens.strip()
            if itens_clean in lista_compras:
                lista_compras.remove(itens_clean)
                print(f"item {itens_clean} removido", end="\n")
            else:
                print(f"item {itens_clean} nao  esta na lista")

    elif response == 3:
        for itens in lista_compras:
            print(f"{itens} ", end="\n")

    elif response == 4:
        print("operação finalizada")
        break
    else:
        print("Opção inválida")


