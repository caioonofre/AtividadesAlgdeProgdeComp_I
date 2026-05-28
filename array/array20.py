tabela = [
    [9, 72, 223, 469, 5],
    [7, 67, 8, 98, 69],
    [11, 55, 13, 0, 99],
    [0, 1, 237, 2, 20]
]

soma_linhas = []
for linha in tabela:
    soma_linha = sum(linha)
    soma_linhas.append(soma_linha)

soma_total = sum(soma_linhas)
print("Soma de cada linha:")
for i, soma in enumerate(soma_linhas):
    print(f"Linha {i + 1}: {soma}")
print(f"Soma total de todos os elementos: {soma_total}")