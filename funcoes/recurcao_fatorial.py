"""
recurção sao funcoes que chaman a si mesma

"""

def regression(n):

    if n > 0:
        print(n)
        regression(n-1)


#regression(10)


"""
fatorial é uma numero multiplicado por todos os seus antecessores

"""

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))
