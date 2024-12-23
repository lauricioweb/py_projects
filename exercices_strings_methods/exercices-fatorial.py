num = int(input("digite um numero"))

""" init = 1
result = 0
for i in range(1,num + 1):
  print(f"{init} X {i}")
  result = init * i
  init = result
  print(init) """


fatorial = 1
for multiplicador in range(1,num + 1):
   fatorial *= multiplicador

   print(f"{multiplicador}", end=" ")

   for i in range(1, multiplicador + 1):
     print(i, end=" ")
     
     if i != multiplicador:
        print(" * ", end="")

   print("=",fatorial)