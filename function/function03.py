def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 6.0:
        print(f"Média: {media:.2f}")
        print("PARABÉNS! Você foi aprovado!")
    else:
        print(f"Média: {media:.2f}")
        print("Infelizmente, você não foi aprovado.")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

calcular_media(nota1, nota2)
