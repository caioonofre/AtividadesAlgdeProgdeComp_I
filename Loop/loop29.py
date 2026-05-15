print("Competição de Pesca")

limite = float(input("Digite o limite diário em Kg: "))

total_gramas = 0

while True:
    peso = float(input("Digite o peso do peixe em gramas: "))

    total_gramas += peso

    total_kg = total_gramas / 1000

    print(f"Peso total da pesca: {total_kg:.2f} Kg")

    if total_kg > limite:
        print("Limite diário excedido!")
        break

    continuar = input("Informar o peso de mais um peixe? (s/n): ").lower()

    if continuar == "n":
        break