def polegadas_para_centimetros(polegadas):
    centimetros = polegadas * 2.54
    return centimetros


# Programa de teste
polegadas = float(input("Digite o valor em polegadas: "))
centimetros = polegadas_para_centimetros(polegadas)
print(f"{polegadas} polegadas equivalem a {centimetros} centímetros.")
