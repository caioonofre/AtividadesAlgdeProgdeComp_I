neg = 0
cont = 2

n = int(input("Insira o 1° numero para saber quantos são negativos: "))
while n != 0:
  if n <0:
    neg+=1
  n = int(input(f'Insira o {cont}° numero para saber quantos são negativos [0 para parar]: '))
  cont+=1

print(f'São {neg} números negativos')