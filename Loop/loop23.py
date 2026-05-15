primeiro = True

clientes = []

nome = input("Digite o nome do cliente: ")

while nome.lower() != "ultimo":
    if primeiro:
        primeiro = False
    else:
        nome = input("\nDigite o nome do cliente: ")

    endereco = input("Digite o endereço: ")
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if valor_compra > 500:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.15

    total_pagar = valor_compra - desconto

    clientes.append(
        {
            "nome": nome,
            "endereco": endereco,
            "valor_compra": valor_compra,
            "desconto": desconto,
            "total_pagar": total_pagar,
        }
    )

if clientes:
    print("\n--- CLIENTES CADASTRADOS ---\n")

    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"Valor da compra: R$ {cliente['valor_compra']:.2f}")
        print(f"Desconto: R$ {cliente['desconto']:.2f}")
        print(f"Total a pagar: R$ {cliente['total_pagar']:.2f} \n")
