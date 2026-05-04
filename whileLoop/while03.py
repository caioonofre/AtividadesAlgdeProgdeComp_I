primeiro = True

num = int(input("Digite um número positivo (0 para encerrar): "))

while num != 0:
    if primeiro:
        maior = num
        menor = num
        primeiro = False
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    num = int(input("Digite outro número (0 para encerrar): "))

print("Maior valor:", maior)
print("Menor valor:", menor)