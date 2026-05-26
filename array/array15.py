VET = []

for i in range(20):
    valor = float(input(f"Digite o {i + 1}° valor: "))
    VET.append(valor)

for i in range(20):
    for j in range(i + 1, 20):
        if VET[i] > VET[j]:
            aux = VET[i]
            VET[i] = VET[j]
            VET[j] = aux

print("\nVetor em ordem crescente:")
for valor in VET:
    print(valor)
