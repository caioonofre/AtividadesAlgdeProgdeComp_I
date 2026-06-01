import random

producao = [[random.randint(1, 50) for _ in range(2)] for _ in range(12)]

custo_lucro = [
    [10, 3],
    [15, 2],
]


def multiplicar_matrizes(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    if n != len(B):
        raise ValueError(
            "Número de colunas de A deve ser igual ao número de linhas de B"
        )

    resultado = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


custo_lucro_mensal = multiplicar_matrizes(producao, custo_lucro)
custo_lucro_anual = [sum(col) for col in zip(*custo_lucro_mensal)]

print("Custo e Lucro Mensal (em milhares de reais):")
for i, (custo, lucro) in enumerate(custo_lucro_mensal):
    print(f"Mês {i + 1}: Custo = {custo}, Lucro = {lucro}")

print("\nCusto e Lucro Anual (em milhares de reais): ")
print(f"Custo Anual = {custo_lucro_anual[0]}, Lucro Anual = {custo_lucro_anual[1]}")
