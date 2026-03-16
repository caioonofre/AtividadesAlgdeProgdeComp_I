# 7. Construir um algoritmo para ler o raio de uma circunferência e mostrar o perímetro ( 2 x π x raio ) e a área ( π x raio2). Utilize o π como constante.
print("Medidas de uma cricunferência!\n")

raio = float(input("Insira o valor do raio da circunferência[cm]: " ))
pi = 3.14159


print(f'\nO valor do perímetro da circunferência de raio {raio}cm é: {round(2*pi*raio, 2)}cm')
print(f'O valor da área da crincuferência de raio {raio}cm é: {round(pi*(raio**2), 2)}cm3')
