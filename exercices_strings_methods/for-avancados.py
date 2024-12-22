"""
nested loops = aninhar um ou mais loops dentro de outro
"""

""" for i in range(1,4):

  for j in range(1,4):

    print(i, "*", j, "=", i*j) """


#imprimindo quadrados impares

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

