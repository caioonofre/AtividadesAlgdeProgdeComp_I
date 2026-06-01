estrutura = [[0 for _ in range(30)] for _ in range(10)]

for i in range(10):
    for j in range(30):
        estrutura[i][j] = i + j

for linha in estrutura:
    print(linha)
