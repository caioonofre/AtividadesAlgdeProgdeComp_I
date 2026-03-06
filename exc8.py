print("Calculadora de imposto de um carro")

carro = float(input("Insira o valor de fabrica do carro: "))
imposto_distrib = round(float(carro*0.28), 2)
imposto_governo = round(float(carro*0.45), 2)

print(f'\nO valor de fabrica do carro é: R${carro}\nA parte do distribuidor é: R${imposto_distrib}\nO valor de imposto é: R${imposto_governo}\n\no valor do carro para consumidor é: R${carro+imposto_distrib+imposto_governo}')
