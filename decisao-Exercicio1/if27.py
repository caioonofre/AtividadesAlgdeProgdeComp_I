# Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor
# inteiro e positivo e a, b, c são quaisquer valores reais. Escreva os valores lidos da
# seguinte maneira:
print("Ordenação de valores\n")
opção = int(input("Insira a opção: "))
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

if opção == 1:
  print(f'Opção 1: Crescente\n a: {a} b: {b} c: {c}\n')
  if a > b and b > c:
    print(f'{c} {b} {a}')
  elif a > c and c > b:
    print(f'{b} {c} {a}')
  elif b > a and a > c:
    print(f'{c} {a} {b}')
  elif b > c and c > a:
    print(f'{a} {c} {b}')
  elif c > a and a > b:
    print(f'{b} {a} {c}')
  elif c > b and b > a:
    print(f'{a} {b} {c}')
elif opção == 2:
  print(f'Opção 2: Decrescente\n a: {a} b: {b} c: {c}\n') 
  if a > b and b > c:
    print(f'{a} {b} {c}')
  elif a > c and c > b:
    print(f'{a} {c} {b}')
  elif b > a and a > c:
    print(f'{b} {a} {c}')
  elif b > c and c > a:
    print(f'{b} {c} {a}')
  elif c > a and a > b:
    print(f'{c} {a} {b}')
  elif c > b and b > a:
    print(f'{c} {b} {a}')
elif opção == 3:
  print(f'Opção 3: Maior valor entre os outros 2\n a: {a} b: {b} c: {c}\n')
  if a > b and a > c:
    print(f'{b} {a} {c}')
  elif b > a and b > c:
    print(f'{a} {b} {c}')
  elif c > a and c > b:
    print(f'{a} {c} {b}')
  else:
    print(f'{a} {b} {c}')
else:
  print("Opção inválida")