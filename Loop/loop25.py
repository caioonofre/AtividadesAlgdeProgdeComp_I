print("Hotel")

contas_encerradas = 0

while True:
    print("\n1. Encerrar conta de um hóspede")
    print("2. Verificar número de contas encerradas")
    print("3. Finalizar execução")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do hóspede: ")
        diarias = int(input("Digite o número de diárias: "))

        if diarias < 15:
            taxa = 7.50
        elif diarias == 15:
            taxa = 6.50
        else:
            taxa = 5.00

        total = diarias * (50 + taxa)

        print(f"\nHóspede: {nome}")
        print(f"Valor total a pagar: R$ {total:.2f}")

        contas_encerradas += 1

    elif opcao == 2:
        print(f"Número de contas encerradas: {contas_encerradas}")

    elif opcao == 3:
        print("Programa finalizado.")
        break

    else:
        print("Opção inválida!")