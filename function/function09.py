def verificar_divisibilidade(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    elif x % y == 0:
        return 1
    else:
        return 0


x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
resultado = verificar_divisibilidade(x, y)
print(f"O resultado da verificação de divisibilidade é: {resultado}")
