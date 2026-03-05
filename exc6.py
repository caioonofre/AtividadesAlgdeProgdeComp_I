print("Calculadora de distância de dois pontos: ")

print("\nPonto 1")
x1 = int(input("Insira o valor x do ponto 1: "))
y1 = int(input("Insira o valor y do ponto 1: "))
x2 = int(input("Insira o valor x do ponto 2: "))
y2 = int(input("Insira o valor y do ponto 2: "))

calculo = ((x2 - x1)**2 + (y2-y1)**2)**0.5

print(calculo)