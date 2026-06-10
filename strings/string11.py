import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavras = [
        "banana",
        "abacaxi",
        "laranja",
        "melancia",
        "uva",
        "morango",
        "pera",
        "cereja",
        "kiwi",
        "manga",
        "amora",
        "framboesa",
        "goiaba",
        "jabuticaba",
        "maracuja",
        "pessego",
        "tangerina",
        "acerola",
        "caju",
        "figo",
        "footebol",
        "basquete",
        "volei",
        "tenis",
        "natação",
        "corrida",
        "ciclismo",
        "boxe",
        "karate",
        "judô",
        "xadrez",
        "damas",
        "poker",
        "blackjack",
        "xadrez",
        "dama",
    ]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("\nDigite uma letra: ").upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"-> Você errou pela {erros}a vez. Tente de novo!\n")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(f"\n{letras_acertadas}")

    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print(f"Game Over! A palavra era {palavra_secreta}.")


jogar()
