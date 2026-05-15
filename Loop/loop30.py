print("Pesquisa de Consumo de Energia")

# Preço do kWh por tipo
preco_r = float(input("Digite o preço do kWh residencial: R$ "))
preco_c = float(input("Digite o preço do kWh comercial: R$ "))
preco_i = float(input("Digite o preço do kWh industrial: R$ "))

n = int(input("Digite a quantidade de consumidores: "))

consumidores = []

total_r = 0
total_c = 0
total_i = 0
total_geral = 0

# Cadastro dos consumidores
for i in range(n):
    print(f"\nConsumidor {i + 1}")

    identificacao = input("Número de identificação: ")
    consumo = float(input("Quantidade de kWh consumidos: "))
    tipo = input("Tipo de consumidor (R/C/I): ").upper()
    tipos = ["R", "C", "I"]

    while tipo not in tipos:
        tipo = input("Isira novamente o tipo de consumidor (R/C/I): ").upper()

    if tipo == "R":
        preco = preco_r
        total_r += consumo
    elif tipo == "C":
        preco = preco_c
        total_c += consumo
    else:
        preco = preco_i
        total_i += consumo

    total_pagar = consumo * preco
    total_geral += consumo

    consumidor = {
        "id": identificacao,
        "consumo": consumo,
        "tipo": tipo,
        "total": total_pagar
    }

    consumidores.append(consumidor)

print("\n--- RESULTADOS ---")

for consumidor in consumidores:
    print(f"""
Identificação: {consumidor["id"]}
Tipo: {consumidor["tipo"]}
Consumo: {consumidor["consumo"]} kWh
Total a pagar: R$ {consumidor["total"]:.2f}
|==|==|==|==|==|==|==|==|==|==|==|==|==|==|==|
""")

print(f"Total consumido Residencial: {total_r} kWh")
print(f"Total consumido Comercial: {total_c} kWh")
print(f"Total consumido Industrial: {total_i} kWh")

media = total_geral / n

print(f"Média geral de consumo: {media:.2f} kWh")