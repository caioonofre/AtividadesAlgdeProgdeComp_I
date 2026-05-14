ingressos = 120
preco_inicial = 5.00
first = True
lucro_maximo = 0
preco_lucro_maximo = 0
ingressos_lucro_maximo = 0

for _ in range(10, 1, -1):
    lucro = preco_inicial * ingressos - 200
    if first or lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_lucro_maximo = preco_inicial
        ingressos_lucro_maximo = ingressos
        first = False
    print(
        f"Preço do ingresso: R$ {preco_inicial:.2f}, Ingressos vendidos: {ingressos}, Lucro: R$ {lucro:.2f}"
    )
    preco_inicial -= 0.50
    ingressos += 26

print(
    f"\nO lucro maximo esperado é de R$ {lucro_maximo:.2f} com o preço do ingresso a R$ {preco_lucro_maximo:.2f} e {ingressos_lucro_maximo} ingressos vendidos."
)
