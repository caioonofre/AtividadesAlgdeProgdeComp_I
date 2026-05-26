# 13) Escreva um algoritmo que:
# a) leia uma frase de 50 caracteres;
# b) conte quantos brancos existem na frase;
# c) conte quantas vezes a letra “A” aparece;
# d) imprima o que foi calculado nos itens b e c.

frase = input("Digite uma frase de até 50 caracteres: ")
if len(frase) > 50:
    print("A frase deve conter no máximo 50 caracteres.")
else:
    contador_brancos = 0
    contador_a = 0

    for caractere in frase:
        if caractere == " ":
            contador_brancos += 1
        elif caractere.upper() == "A":
            contador_a += 1

    print(f"Número de brancos na frase: {contador_brancos}")
    print(f"Número de vezes que a letra 'A' aparece: {contador_a}")
