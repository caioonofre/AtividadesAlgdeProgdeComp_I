def calcular_poligono(lados, medida):
    if lados == 3:
        perimetro = lados * medida
        print(f"TRIÂNGULO - Perímetro: {perimetro} cm")
    elif lados == 4:
        area = medida**2
        print(f"QUADRADO - Área: {area} cm²")
    elif lados == 5:
        print("PENTÁGONO")


num_lados = int(input("Digite o número de lados do polígono (3, 4 ou 5): "))
medida_lado = float(input("Digite a medida do lado (em cm): "))
calcular_poligono(num_lados, medida_lado)
