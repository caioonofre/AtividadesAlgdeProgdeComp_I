# 1. Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área
# ( lado2
# ) e seu perímetro ( 4 x lado ).

print("Transformador de medidas de um quadrado!")

lado = float(input("Insira o valor do lado do quadrado[cm]: "))

print(f'\nO valor do perímetro é {lado*4} cm')
print(f'\nO valor da área é de {lado**2} cm3')