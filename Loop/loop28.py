print("Jogo de Pingue-Pongue")

direita = 0
esquerda = 0

while True:
    ponto = input("Digite o vencedor da jogada (D/E): ").upper()

    if ponto == "D":
        direita += 1
    elif ponto == "E":
        esquerda += 1
    else:
        print("Código inválido!")
        continue

    print(f"Placar -> Direita: {direita} | Esquerda: {esquerda}")

    if (direita >= 21 or esquerda >= 21) and abs(direita - esquerda) >= 2:
        break

if direita > esquerda:
    print("\nVencedor: Jogador da Direita")
else:
    print("\nVencedor: Jogador da Esquerda")