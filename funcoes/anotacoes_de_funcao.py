"""
documentação e anotações de função

- docstrings 
- anotações de tipo (typehint)

1 - Docstrings são usadas para documentar especificamente oque uma função faz, seus parametros e o que ela retorna. eles sao colocados logo apos a definição da função, antes do codigo da função
começar, e são escritos em aspasm duplas ""

"""

# exemplos

def soma(x,y):
    """
    função que retorna a soma de dois numeros

    parametros:

    x (int ou float): primeiro numero
    y (int ou float): segundo numero
    
    retorna (int ou float)

    """

    return x + y

#print(soma(2,4))
#print(soma.__doc__)


"""
 2 - anotações de tipo são usadas para indicar os tipos esprados dos argumentos e o tipo de retorno de uma função. elas não causam nenhuma verificação de tipo  de execução, mas são uteis para
 documentação e ferramentas de verificação estetrica de tipo como o mypy

 exemplo:

"""

def multiplicar(a:int, b:int):
    return a * b 


#usar sempre a combinação de docstring e typehinit


