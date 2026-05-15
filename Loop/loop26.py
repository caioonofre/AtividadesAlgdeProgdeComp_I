massa = float(input("Digite a massa inicial em Kg: "))

massa_inicial = massa
tempo = 0

while massa >= 0.0005:
    massa = massa / 2
    tempo += 50

print(f"Massa inicial: {massa_inicial:.6f} Kg")
print(f"Massa final: {massa:.6f} Kg")
print(f"Tempo necessário: {tempo} segundos")