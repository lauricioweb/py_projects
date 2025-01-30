""" funções lambda sao funções anonimas de pequena extensão  ao contrario de uma fução definida com def. a função lambda podem ter apenas uma expressão e retorna implicitamente o resultado
dessa expressao. ela é frequentemente usada  para pequenas operações que são convenientes de se definir sem nomear  uma função completa.

"""


### funcao regular 

def dobrar(n):
    return n * 2


print(f"funcao regular> {dobrar(5)}")


### usando funcao lambda

dobrarLamb = lambda n: n * 2


print(f"funcao lambda> {dobrarLamb(5)}")


### condições em funções lambda 

### funcao regular

def number_inf(n):

    if n > 0:
        return "positivo"

    elif n == 0:
        return "zero"

    else:
        return "negativo"



print(f"funcao regular numero info {number_inf(10)}")

### funcao lambda

lamb_number_info = lambda n: "positivo" if n > 0 else (" zero" if n == 0 else "negativo") 

print(f"funcao lambda numero info {lamb_number_info(10)}")



























