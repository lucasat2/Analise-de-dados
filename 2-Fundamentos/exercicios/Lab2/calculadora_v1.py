# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("\n Selecione o número da operacao desejada:")

print("\n 1 - Soma")
print("\n 2 - Subtração")
print("\n 3 - Multiplicação")
print("\n 4 - Divisão")

opcao = int(input("Digite a sua opção(1/2/3/4): "))

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


if(opcao == 1) :
  res = num1 + num2 
  print(num1 ,"+", num2 ,"=", res)

if(opcao == 2) : 
  res = num1 - num2
  print(num1 ,"-", num2 ,"=", res)

if(opcao == 3) :
  res = num1 * num2
  print(num1 ,"*", num2 ,"=", res)

if(opcao == 4) : 
  res = num1 / num2
  print(num1 ,"/", num2 ,"=", res)
