def show_details(**kwargs):
  # **kwargs mostra a chave e valor de um parametro recebido
  for chave, valor in kwargs.items():
    print(chave + " : " + str(valor))

#email = "dev@gmail.com"
show_details(nome="lauricio", idade=33)