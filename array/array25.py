# nesse exercicio usei a biblioteca random para gerar numeros aleatorios para a matriz, a fim de curiosidade.
import random


# Criando a matriz MAT de 4 x 5 de numeros aleatorios
MAT = [
    [random.randint(1, 100) for _ in range(5)] for _ in range(4)
]

SOMALINHA = [0] * 4
for i in range(4):
    SOMALINHA[i] = sum(MAT[i])

TOTAL = sum(SOMALINHA)

print("Matriz MAT:")

for row in MAT:
    print(row)
print("\nVetor SOMALINHA:", SOMALINHA)
print("TOTAL:", TOTAL)

            