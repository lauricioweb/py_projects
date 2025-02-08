# tupas sao um tipo de lista que nao podem ser modificados;

# podem ser declaradas das seguintes formas

  # convencional

t1 = (1,2,3,4,5)

# sem parenteses

t1 = 1, 2, 3, 4

print(type(t1))

# descompactando tupla em varias variaveis

n1, n2, n3, *high, n4 = (1,2,"lau", 44,53,21,"gosma")

print(n3)
print(high)
print(n4)


# convertendo tuplas em listas e listas em tuplas

# uma tupla so pode ser modificada apos ser trasformada em lista

my_tuple = (1,3,67,74)
my_tuple = list(my_tuple)
my_tuple[1] = "goSMA branCA"
my_tuple = tuple(my_tuple)
print(my_tuple)


#lauricio es bom