canal4 = 0
canal5 = 0
canal9 = 0
canal12 = 0
total_pessoas = 0

n = int(input("Digite a quantidade de casas pesquisadas: "))

for i in range(n):
    print(f"\nCasa {i+1}")

    canal = int(input("Digite o canal (4, 5, 9, 12 ou 0 para TV desligada): "))

    while canal != 4 or canal != 5 or canal != 9 or canal != 12:
        canal = int(input("Digite o canal (4, 5, 9, 12 ou 0 para TV desligada): "))

    pessoas = int(input("Digite o número de pessoas assistindo: "))

    if canal != 0:
        total_pessoas += pessoas

        if canal == 4:
            canal4 += pessoas
        elif canal == 5:
            canal5 += pessoas
        elif canal == 9:
            canal9 += pessoas
        elif canal == 12:
            canal12 += pessoas

if total_pessoas > 0:
    print("\nPercentual de audiência:")

    print(f"Canal 4: {(canal4 / total_pessoas) * 100:.2f}%")
    print(f"Canal 5: {(canal5 / total_pessoas) * 100:.2f}%")
    print(f"Canal 9: {(canal9 / total_pessoas) * 100:.2f}%")
    print(f"Canal 12: {(canal12 / total_pessoas) * 100:.2f}%")
else:
    print("Nenhuma TV estava ligada.")