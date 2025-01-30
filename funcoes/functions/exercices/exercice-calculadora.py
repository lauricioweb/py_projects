def factoryFunction(operation):

  def soma(*args):

    return sum(args)
  
  def sub(*args):

    resultado = args[0]
    
    for num in args[1:]:
      resultado -= num

    return resultado
  
  def mult(*args):
    resultado = args[0]
    
    for num in args[1:]:
      resultado *= num
    
    return resultado

  def divisao(*args):
    resultado = args[0]
    
    for num in args[1:]:
      
      if num == 0:
        raise ValueError("nao é possivel dividir por 0")
      
      resultado /= num
    
    return resultado

  def errorOperation(*args):
    return "operação invalida!"


   ### as funções abaixo nao estao sendo chamadaas sem a nescessidade de passar argumentos/ estao apenas sendo retornadas
  if operation == "soma":
    return soma
  
  elif operation == "subtrair":
    return sub
  
  elif operation == "mult":
    return mult 

  elif operation == "divisao":
    return divisao

  else:
    return errorOperation
  
  

myoperation = factoryFunction("divisao2")

result = myoperation(10,2,0)
print(result)