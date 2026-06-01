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
    print(f'Soma de A + _: {contador_brancos + contador_a}')
