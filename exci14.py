print("Calculadora de cerca!")
print("\nInsira a medida dos 4 lados do seu terreno: \n")
medida1 = float(input("Medida 1: "))
medida2 = float(input("Medida 2: "))
medida3 = float(input("Medida 3: "))
medida4 = float(input("Medida 4: "))
perimetro = medida1+medida2+medida3+medida4


mourao = float(input("\nInsira o valor de um mourão: "))
qtd_mourao = perimetro//3
arame = float(input("Insira o valor do metro do arame farpado: "))
qtd_arame = round(perimetro*4)

print(f'\nO Perímetro do seu terreno é de {perimetro}\nA quantidade de mourões gastos é de {qtd_mourao}, gastando o valor de R${mourao*qtd_mourao}.\nA quantidade de arame é de {qtd_arame} metros, gastando o valor de R${arame*qtd_arame}\nO valor total para cercar o seu terredo é de R${(mourao*qtd_mourao)+(arame*qtd_arame)}!')

