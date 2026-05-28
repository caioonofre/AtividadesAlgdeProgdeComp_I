def pesquisa_binaria(vetor, chave):
    esquerda, direita = 0, len(vetor) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

vetor = []
print("Digite 10 elementos para o vetor (em ordem crescente):")
for _ in range(10):
    elemento = int(input())
    vetor.append(elemento)
chave = int(input("Digite a chave K: "))

posicao = pesquisa_binaria(vetor, chave)
if posicao != -1:
    print(f"CHAVE K ENCONTRADA NA POSIÇÃO: {posicao}")
else:
    print("CHAVE K NÃO ENCONTRADA")


