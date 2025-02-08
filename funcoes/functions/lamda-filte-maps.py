# crinado funcao que retorna apenas numeros pares

numbers_list = [1,3,4,2,10,12,16,20]

def number_divisible(numbers):
  
  pair = []
  for num in numbers:

    if num % 2 == 0:
      pair.append(num)

    
  return pair


# print(number_divisible(numbers_list))


# usando filter para obter apenas numeros pares
numbers_p = [1,2,3,4,5,6,7,8,9,10,12,16]

numbers_pair = list(filter(lambda x: x % 2 == 0, numbers_p))
#filter recebe como primeiro parametro uma função que ira validar se cada item do array passado como segundo parametro  cumpre os requisitos da função.

# a funcao passada no primeiro parametro é chamada para cada item.  


# o filter retorna um objeto iteravel, por isso usamos o list() para converter para array,

print(numbers_pair)