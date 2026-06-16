def peso_ideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso = (72.7 * altura) - 58
    else:
        return "Sexo inválido"

    return f"O peso ideal é: {peso:.2f} kg"


altura = float(input("Digite a altura em metros: (ex: 1.75): "))
sexo = int(input("Digite o sexo (1 para feminino, 2 para masculino): "))

resultado = peso_ideal(altura, sexo)
print(resultado)
