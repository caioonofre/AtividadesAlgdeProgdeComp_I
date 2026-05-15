print("Hotel")

diarias = int(input("Digite o número de diárias: "))

if diarias < 15:
    taxa = 7.50
elif diarias == 15:
    taxa = 6.50
else:
    taxa = 5.00

total = diarias * (50 + taxa)

print(f"Valor total a pagar: R$ {total:.2f}")
