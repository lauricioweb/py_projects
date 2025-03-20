
agenda = []

while True:
    print("MENU \n")
    print("1- ADICIONAR CONTATO ")
    print("2- ALTERAR CONTATO ")
    print("3- REMOVER CONTATO ")
    print("4- LISTAR CONTATOS ")
    print("5- SAIR \n")

    option = int(input("Insira a opção desejada: "))

    if option == 1:
        nome = str(input("insira o nome: ")).lower()
        numero = str(input("insira o numero: "))

        contato = {
            "nome":nome,
            "numero":numero
        }

        agenda.append(contato)
        print("contato salvo com sucesso!")
    
    elif option == 2:
        contato = str(input("insira o nome do contato a ser editado: ")).lower()

        for consulta_contato in agenda:
            if contato in consulta_contato["nome"]:
                novo_nome = str(input("insira o novo nome: ")).lower()
                novo_numero = str(input("insira o novo numero: "))
                consulta_contato["nome"] = novo_nome
                consulta_contato["numero"] = novo_numero
                print("contato atualizado")
            elif contato not in consulta_contato["nome"]:
                print("contato não encontrado")
    
    elif option == 3:
        contato = str(input("qual contato voce quer remover ?")).lower()
        
        for consulta_contato in agenda:
            if contato == consulta_contato["nome"]:
                agenda.remove(consulta_contato)
            print("contato removido com sucesso")
    
    elif option == 4:
        print("---- CONTATOS ----")
        for contato in agenda:
            print(f"nome: {contato['nome']} numero: {contato['numero']}")
    
    elif option == 5:
        print("programa encerrado, até mais!")
        break
    
    else: 
        print("OPÇÃO INVALIDA")




