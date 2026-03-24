print("Escolha uma operação: \n0- Soma\n1- subtração\n2- Multiplicação\n3- Divisão\n4- Média")
opcao = int(input("Digite um valor de 0 a 4: "))

if opcao in [0, 1, 2, 3, 4]:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    if opcao == 0:
        resultado = n1 + n2
        print(f"Soma: {resultado}")
    elif opcao == 1:
        resultado = n1 - n2
        print(f"Subtração: {resultado}")
    elif opcao == 2:
        resultado = n1 * n2
        print(f"Multiplicação: {resultado}")
    elif opcao == 3:
        if n2 != 0:
            resultado = n1 / n2
            print(f"Divisão: {resultado}")
        else:
            print("Erro: divisão por zero.")
    elif opcao == 4:
        resultado = (n1 + n2) / 2
        print(f"Média: {resultado}")
else:
    print("Valor errado. Programa encerrado sem cálculos")