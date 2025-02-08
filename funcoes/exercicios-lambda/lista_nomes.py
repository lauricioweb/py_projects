"""
criar funcao lambda que  filtra uma lista de string obtendo em um array apenas os nomes que começam com 
a letra A 

"""

names_list = ["Alana", "Beatriz", "amanda", "aline","raissa"]


# funcao convecional

def filter_names (names):

    names_filtered = []

    for name in names:
        if name[0] == "A":
            names_filtered.append(name)

    return names_filtered


names_filtered = filter_names(names_list)

# print(names_filtered)


lambda_filter = list(filter(lambda x: x[0] == "A" or x[0] == "a" , names_list))

print(lambda_filter)
