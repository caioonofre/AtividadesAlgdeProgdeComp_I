matriz = []
print("Digite os elementos da matriz (6 linhas e 3 colunas):")
for i in range(6):
    linha = []
    for j in range(3):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Calculando o somatório dos elementos da quinta linha (índice 4)
somatorio = sum(matriz[4])  # A quinta linha tem índice 4
print(f"O somatório dos elementos da quinta linha é: {somatorio}")
