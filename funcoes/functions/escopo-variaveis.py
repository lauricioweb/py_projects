"""
variaveis locais vs globais

variaveis globais são criadas fora de funções ou laços, podem
ser acessadas em qualquer parte do codigo
variaveis locais são criadas dentro de função e so podem ser acessadas dentro do escopo desta função
"""

# usando a palavra global para modificar variaveis globais

global_variable = "variavel global"

def show():
  local_variable = "variavel local"

  global global_variable
  
  print(local_variable)
  # uma variavel global pode ser acessada em qualquer parte do codigo.
  print(global_variable)

  # mas para modifica-la usa se a referencia global antes de modificar

  global_variable = "teste de texto"

  print(global_variable)


#show()

"""
usando  variavel global
"""


contador = 1

def addContador():
    global contador

    contador += 1
    print(contador)


#addContador()
#addContador()


"""
variavel nonlocal
são variaveis criadas dentro de uma função que serão modificadas
dentro de uma  função aninhada para isso usa se a palavra chave "nonlocal"
e então esta varival sera modificada dentro de uma função interna

"""

def externfunc():
    variavelExterna = "sou uma variavel extertan"
    print(variavelExterna)

    def internFunc():
        nonlocal variavelExterna

        variavelExterna = "fui modificada por uma função interna"

        print(variavelExterna)

    internFunc()
    print(variavelExterna)

externfunc()





