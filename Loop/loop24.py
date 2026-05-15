print("Cálculo da média das idades")

soma = 0
quantidade = 0

continuar = "s"

while continuar.lower() == "s":
    idade = int(input("Digite uma idade: "))

    if idade > 0:
        soma += idade
        quantidade += 1

    continuar = input("Deseja digitar mais um valor: s (SIM) / n (NAO)? ").lower()

if quantidade > 0:
    media = soma / quantidade
    print(f"Foram inseridos {quantidade} idades | Idade média do grupo: {media:.2f}")
else:
    print("Nenhuma idade válida foi digitada.")
