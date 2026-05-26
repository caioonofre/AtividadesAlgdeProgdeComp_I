quantidade = []
preco = []
faturamento = 0

for i in range(10):
    qnt = int(input(f"Digite a quantidade vendida da mercadoria {i}: "))
    quantidade.append(qnt)

for i in range(10):
    valor = float(input(f"Digite o preço da mercadoria {i}: "))
    preco.append(valor)

for i in range(10):
    faturamento += quantidade[i] * preco[i]

print(f"\nFaturamento mensal = R$ {faturamento:.2f}")
