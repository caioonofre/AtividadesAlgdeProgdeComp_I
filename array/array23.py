matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("Matriz 5 x 5:")
for linha in matriz:
    print(linha)

soma = 0
for i in range(5):
    for j in range(i + 1):
        soma += matriz[i][j]
print(f"Soma dos elementos abaixo da diagonal principal (incluindo a diagonal): {soma}")

