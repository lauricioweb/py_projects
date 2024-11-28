# adivinhando dois numeros

numeroSecreto1 = 4
numeroSecreto2 = 3

tentativas = 5

advinhou1 = False
advinhou2 = False

while tentativas > 0 and (not advinhou1 or not advinhou2):
  print(f"tentativas restantes {tentativas}")

  palpite1 = int(input("qual o primeiro numero ?"))
  palpite2 = int(input("qual o segundo numero ?"))

# se o palpite é igual ao numero secreto
  if palpite1 == numeroSecreto1:

    print("voce advinhou o primeiro numero")
    advinhou1 = True

 # se o palpite é igual ao numero secreto
  if palpite2 == numeroSecreto2:

    print("voce advinhou o primeiro numero")
    advinhou2 = True


 # reduzindo tentativas caso os numeros sejam incorretos
  if not advinhou1 or not advinhou2:

    print("tente novamente !")
    tentativas -= 1

# verificando se os numeros estão corretos
if advinhou1 and advinhou2:
  print("parabens voce acertou os dois numeros !")
else:
  print(f"você na conseguiu acertar \n primeiro numero era {numeroSecreto1}  e o segundo era {numeroSecreto2}")