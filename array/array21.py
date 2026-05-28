k = int(input("Digite a constante k para multiplicar os elementos da diagonal principal: "))

matriz = []
print("Digite os elementos da matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)
for i in range(4):
    matriz[i][i] *= k

print("\nMatriz resultante após multiplicar a diagonal principal por k:")
for i in range(4):
    for j in range(4):
        if i == j:
            print(f"\033[1m{matriz[i][j]}\033[0m", end=" ")
        else:
            print(f"{matriz[i][j]}", end=" ")
    print()
