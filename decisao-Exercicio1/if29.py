print("Calculadora de reajuste salarial\n")
salario = float(input("Insira o salário atual do funcionário: "))
if salario < 10000.00:
  aumento = salario*0.55
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
else:
  aumento = salario*0.20
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")