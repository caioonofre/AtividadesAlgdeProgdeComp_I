# Criar um algoritmo para ler a base e a altura de um triângulo e
# mostrar a sua área ( ( base x altura ) / 2 ).

print("Medidas de um triângulo!\n")

base = float(input("Insira a base do triângulo[cm]: "))
altura = float(input("Insira a altura do triângulo[cm]: "))

print(f'\nA área do triângulo com base de {base} e a altura {altura} é: {(base*altura)/2} cm2')