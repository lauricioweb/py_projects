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


  if operation == "soma":
    return soma
  
  elif operation == "subtrair":
    return sub
  
  elif operation == "mult":
    return mult 

  elif operation == "divisao":
    return divisao
  
  

myoperation = factoryFunction("divisao")

result = myoperation(10,2)
print(result)