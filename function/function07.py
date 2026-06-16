def mes_correspondente(numero):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }
    return meses.get(
        numero, "Número inválido. Por favor, insira um número entre 1 e 12."
    )


numero = int(input("Digite um número inteiro para o mês (1-12): "))
resultado = mes_correspondente(numero)
print(resultado)
