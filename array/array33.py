# 33) Faça um algoritmo que leia uma matriz QUANT de 10 linhas por 10 random colunas e imprima as
# seguintes características:
# a) dê o somatório dos quadrados da 1a coluna;
# b) dê o somatório dos cubos da 2a linha;
# c) dê o somatório dos elementos da diagonal principal;
# d) dê o somatório total dos 100 elementos.
import random

QUANT = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
soma_quadrados_coluna1 = 0
soma_cubos_linha2 = 0
soma_diagonal_principal = 0
soma_total = 0

print("Matriz QUANT:")
for i in range(10):
    print(f"QUANT[{i}] = {QUANT[i]}")

for i in range(10):
    for j in range(10):
        soma_total += QUANT[i][j]
        if j == 0:
            soma_quadrados_coluna1 += QUANT[i][j] ** 2
        if i == 1:
            soma_cubos_linha2 += QUANT[i][j] ** 3
        if i == j:
            soma_diagonal_principal += QUANT[i][j]
print("")

print("\nResultados:")
print("-----------------------------")
print(f"Somatório dos quadrados da 1a coluna: {soma_quadrados_coluna1}")
print(f"Somatório dos cubos da 2a linha: {soma_cubos_linha2}")
print(f"Somatório dos elementos da diagonal principal: {soma_diagonal_principal}")
print(f"Somatório total dos 100 elementos: {soma_total}")
