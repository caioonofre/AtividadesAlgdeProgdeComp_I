def numero_por_extenso(numero):
    if numero < 0 or numero > 99:
        return "Número fora do intervalo permitido. Digite um número entre 0 e 99."

    unidades = [
        "zero",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
    ]
    dezenas = [
        "dez",
        "onze",
        "doze",
        "treze",
        "quatorze",
        "quinze",
        "dezesseis",
        "dezessete",
        "dezoito",
        "dezenove",
    ]
    dezenas_maiores = [
        "vinte",
        "trinta",
        "quarenta",
        "cinquenta",
        "sessenta",
        "setenta",
        "oitenta",
        "noventa",
    ]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return dezenas[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10
        if unidade == 0:
            return dezenas_maiores[dezena - 2]
        else:
            return dezenas_maiores[dezena - 2] + " e " + unidades[unidade]


numero = int(input("Digite um número entre 0 e 99: "))
print(numero_por_extenso(numero))
