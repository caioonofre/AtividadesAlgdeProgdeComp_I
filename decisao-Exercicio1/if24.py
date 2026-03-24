print("Calculadora\n")
valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))
operação = int(input("Insira a operação a ser executada[1, 2, 3, 4]: "))

if operação == 1:
  print(f'O resultado da adição {valor1} + {valor2} é: {valor1 + valor2}')
elif operação == 2:
  print(f'O resultado da subtração {valor1} - {valor2} é: {valor1 - valor2}')
elif operação == 3:
  print(f'O resultado da multiplicação {valor1} * {valor2} é: {valor1 * valor2}')
elif operação == 4:
  print(f'O resultado da divisão {valor1} / {valor2} é: {valor1 / valor2}')
else:
  print("Operação inválida")