# loops aninhados

linha = 0

while linha < 3:
    coluna = 0 #esta variavel so sera alterada apos o sair do loop abaixo
     
    while coluna < 3: 
        print(f"linha {linha} coluna {coluna}")
        coluna += 1
         
    linha += 1
