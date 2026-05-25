numeros = []
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

posicoes_30 = [index for index, numero in enumerate(numeros) if numero == 30]
if posicoes_30:
    print(
        f"{len(posicoes_30)} Elementos iguais a 30 encontrados nas posições: {posicoes_30}"
    )
else:
    print("Nenhum elemento igual a 30 encontrado.")
