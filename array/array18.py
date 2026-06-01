matriz = []
print("Digite os elementos da matriz (15 linhas e 25 colunas):")
for i in range(5):
    linha = []
    for j in range(5):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("Conteúdo da matriz:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=' ')
    print()