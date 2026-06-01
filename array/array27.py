
# Programa simples sem funções — estoque e custos predefinidos

# Matriz de estoque: linhas = armazéns, colunas = produtos
# Valores conforme tabela do enunciado
estoque = [
    [1200, 3700, 3737],
    [1400, 4210, 4224],
    [2000, 2240, 2444]
]

# Custos por produto (R$)
custos = [260.00, 420.00, 330.00]

print('a) Estoque inicial (linhas = armazéns, colunas = produtos):')
for i, linha in enumerate(estoque, start=1):
    print(f'Armazém {i}:', ' '.join(str(x) for x in linha))

print('\n b) Quantidade total armazenada em cada armazém:')
totais_por_armazem = []
for i, linha in enumerate(estoque, start=1):
    total = sum(linha)
    totais_por_armazem.append(total)
    print(f'Armazém {i}: {total} unidades')

# c) armazém com maior quantidade do produto 2 (índice 1)
produto2 = [estoque[i][1] for i in range(len(estoque))]
maior_qtd = max(produto2)
armazem_maior = produto2.index(maior_qtd) + 1
print(f"\n c) Armazém com maior quantidade do Produto 2: Armazém {armazem_maior} ({maior_qtd} unidades)")

print('\n d) Cálculo de custos:')

print('\n d.1) Custo de cada produto em cada armazém:')
for i, linha in enumerate(estoque, start=1):
    custos_por_produto = [linha[j] * custos[j] for j in range(len(custos))]
    custos_str = '  '.join(f'R$ {c:.2f}' for c in custos_por_produto)
    print(f'Armazém {i}: {custos_str}')

print('\n d.2) Custo total em cada armazém:')
for i, linha in enumerate(estoque, start=1):
    total_custo = sum(linha[j] * custos[j] for j in range(len(custos)))
    print(f'Armazém {i}: R$ {total_custo:.2f}')

print('\n d.3) Cada produto em todos os armazéns (unidades e custo total):')
for j in range(len(custos)):
    total_unidades = sum(estoque[i][j] for i in range(len(estoque)))
    total_custo = total_unidades * custos[j]
    print(f'Produto {j+1}: {total_unidades} unidades - Custo total R$ {total_custo:.2f}')
