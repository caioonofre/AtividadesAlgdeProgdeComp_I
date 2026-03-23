valorProd = float(input("Insira o valor do produto: "))

if valorProd < 20:
  valorProd += valorProd*0.45
  print(f'O valor final do prduto é: R$ {valorProd}')
else:
  valorProd += valorProd*0.30
  print(f'O valor final do prduto é: R$ {valorProd}')