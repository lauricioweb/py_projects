#function args pode ser usafa para receber parametros em uma lista

def somaArgs(*args):
  return sum(args)


print(somaArgs(1,2,3,4))