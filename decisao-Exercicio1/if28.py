print("Calculadora de aumento de salário\n")
salario = float(input("Insira o salário atual do funcionário: "))
if salario <= 400.00:
  aumento = salario*0.15
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
elif salario <= 700.00 and salario > 400.00:
  aumento = salario*0.12
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
elif salario <= 1000.00 and salario > 700.00:
  aumento = salario*0.10
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
elif salario <= 1500.00 and salario > 1000.00:
  aumento = salario*0.07
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
elif salario <= 2000.00 and salario > 1500.00:
  aumento = salario*0.04
  salario += aumento
  print(f"O salário atual do funcionário é: {salario} e o aumento é de: {aumento}")
else:
  print(f"O salário atual do funcionário é: {salario} e não tem aumento")