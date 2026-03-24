print("Ordem crescente\n")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
  print(f'{n1} {n2}')
elif n2 > n1:
  print(f'{n2} {n1}')
else:
  print("Os números são iguais")