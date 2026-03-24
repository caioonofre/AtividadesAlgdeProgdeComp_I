print("Soma dos dois maiores\n")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if n1 > n2 and n1 > n3:
  print(f'A soma dos dois maiores é: {n2 + n3}')
elif n2 > n1 and n2 > n3:
  print(f'A soma dos dois maiores é: {n1 + n3}')
else:
  print(f'A soma dos dois maiores é: {n1 + n2}')