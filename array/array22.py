matriz = []
print("Digite os elementos da matriz 5x5:")
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

for i in range(5):
    diagonal_element = matriz[i][i]
    for j in range(5):
        matriz[i][j] /= diagonal_element
print("\nMatriz resultante após dividir cada elemento da linha pelo elemento da diagonal principal:")
for i in range(5):
    for j in range(5):
        if i == j:
            print(f"\033[1m{matriz[i][j]:.2f}\033[0m", end=" ")
        else:
            print(f"{matriz[i][j]:.2f}", end=" ")
    print()
