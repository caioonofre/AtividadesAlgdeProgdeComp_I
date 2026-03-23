idade = int(input("Insira sua idade: "))

if idade < 18 and idade > 0:
    print("Menor de idade!")
elif idade >= 18 and idade < 65:
    print("Maior de idade!")
elif idade >= 65:
    print("Idoso acima de 65")
elif idade < 1:
    print("Insira uma idade válida")