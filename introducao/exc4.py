import math;
print("Calcular o volume de uma lata de óleo!")

raio = float(input("\nInsira o raio da lata[cm]: "))
altura = float(input("\nInsira a altura[cm]: "))
volume = round(math.pi * (raio*raio) * altura, 2)

print(f'O valor do volume da lata é: {volume} cm3 ou {round(volume/1000, 2)} Litros')