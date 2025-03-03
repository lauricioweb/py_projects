# trasformando listas em strings
string = "texto"
list_str = list(string)

print(list_str)

# convertendo strings para lista com separador especifico

my_str = "lauricio é um exelente programador"

my_list_str = my_str.split() # sem parametro ira se parar por espaços

print(my_list_str)

#transformando listas em string com o join()

str_exp = ["ola", "sou","lauricio"]

str_comp = " ".join(str_exp) # a string vazia é o delimitador entre cada item do array ao ser trasformado em string
print(str_comp)

list_data = ["12","01","2022"]

list_compressed = "/".join(list_data)
print(list_compressed)