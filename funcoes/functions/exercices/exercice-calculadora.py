operacao = input("digita a operação que deseja execultar")

def calculadora(operacao):
  n1 = int(input("digite o numero 1"))
  n2 = int(input("digite o numero 2"))

  def soma(n1,n2):
    return n1 + n2
  
  def subtrai(n1,n2):
    return n1 - n2
  
  def divide(n1,n2):
    return n1 / n2
  
  def multi(n1,n2):
    return n1 * n2
  
  if operacao == "soma":
     return soma(n1,n2)

  elif operacao == "subtrai":
     return subtrai(n1,n2)

  elif operacao == "dividir":
     return divide(n1,n2)

  elif operacao == "multi":
     return multi(n1,n2)


result = calculadora(operacao)
print(result)