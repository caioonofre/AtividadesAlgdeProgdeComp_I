def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5
    return hipotenusa


cateto_a = int(input("Digite o valor do cateto A: "))
cateto_b = int(input("Digite o valor do cateto B: "))
hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print(f"A hipotenusa de catetos {cateto_a} e {cateto_b} é: {hipotenusa}")
