
while True:
   
   operacao = int(input("qual operação a sera realizada? \n 1- adição \n 2- subtração \n 3- divisão \n 4- multiplicação \n 5- sair \n :"))

   if operacao == 5:
      print("até mais !")
      break
   
   num1 = float(int(input("digite o primeiro numero ")))
   num2 = float(int(input("digite o segundo numero ")))

   if operacao == 1:
     print(f"reasultado {num1 + num2}")
   
   elif operacao == 2:
     print(f"reasultado {num1 - num2}")
   
   elif operacao == 3:
     print(f"reasultado {num1 / num2}")
  
   elif operacao == 4:
     print(f"reasultado {num1 * num2}")

      

         
