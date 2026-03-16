print("Conversor de graus! \n")

escolha = input("Qual grau você quer converter?\n\n1) Fahrenheit(°F) -> Celsius(°C)\n2) Celsius(°C)-> Fahrenheit(°F)\n3) Celsius(°C)-> Kelvin(K)\n4) Kelvin(K) -> Celsius(°C)\n escolha: ")

if escolha == "1":
  print("\nConversor de Fahrenheit(°F) -> Celsius(°C)\n")
  grau = float(input("Insira o valor a ser convertido: "))
  print(f'O resultado da conversão de {grau}°F para Celsius(°C) é: {round((grau-32)/1.8, 2)}°C')
elif escolha == "2":
  print("\nConversor de Celsius(°C)-> Fahrenheit(°F)\n")
  grau = float(input("Insira o valor a ser convertido: "))
  print(f'O resultado da conversão de {grau}°C para Fahrenheit(°F) é: {(grau*1.8)+32}°F')
elif escolha == "3":
  print("\nConversor de Celsius(°C)-> Kelvin(K)\n")
  grau = float(input("Insira o valor a ser convertido: "))
  print(f'O resultado da conversão de {grau}°C para Kelvin(K) é: {grau+273.15}K')
elif escolha == "4":
  print("\nConversor de Kelvin(K) -> Celsius(°C)\n")
  grau = float(input("Insira o valor a ser convertido: "))
  print(f'O resultado da conversão de {grau}°K para Celsius(°C) é: {grau-273.15}°C')
else:
  print("Escolha apenas um número de 1 a 4")