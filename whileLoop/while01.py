# Faça um algoritmo que:
# • leia 20 números inteiros;
# • escreva os números que são negativos;
# • escreva a média dos números positivos.
cont = 0
numeros = []

while cont < 5:
    n = int(input(f'Insira o nuemro {cont+1}: '))
    if n >= 0:
        numeros.append(n)
    cont += 1

print(numeros)