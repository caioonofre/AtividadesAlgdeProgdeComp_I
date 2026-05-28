A = []
B = []
Soma = []

print("Digite os valores da matriz A:")
for i in range(3):
    linha = []
    for j in range(5):
        valor = float(input(f"A[{i+1}][{j+1}]: "))
        linha.append(valor)
    A.append(linha)

print("\nDigite os valores da matriz B:")
for i in range(3):
    linha = []
    for j in range(5):
        valor = float(input(f"B[{i+1}][{j+1}]: "))
        linha.append(valor)
    B.append(linha)

print("\nMatriz A:")
for i in range(3):
    for j in range(5):
        print(f"{A[i][j]:.2f}", end=" ")
    print()
    
print("\nMatriz B:")
for i in range(3):
    for j in range(5):
        print(f"{B[i][j]:.2f}", end=" ")
    print()

for i in range(3):
    linha_soma = []
    for j in range(5):
        soma_valor = A[i][j] + B[i][j]
        linha_soma.append(soma_valor)
    Soma.append(linha_soma)

print("\nSoma das matrizes A e B:")
for i in range(3):
    for j in range(5):
        print(f"{Soma[i][j]:.2f}", end=" ")
    print()
