def encontrar_chave(vetor, chave):
    for i in range(len(vetor)):
        if vetor[i] == chave:
            return i
    return -1


vetor = []
print("Digite 10 elementos para o vetor:")
for _ in range(10):
    elemento = int(input())
    vetor.append(elemento)
chave = int(input("Digite a chave K: "))

posicao = encontrar_chave(vetor, chave)
if posicao != -1:
    print(f"CHAVE K ENCONTRADA NA POSIÇÃO: {posicao}")
else:
    print("CHAVE K NÃO ENCONTRADA")
