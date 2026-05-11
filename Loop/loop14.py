soma = 1
sinal = -1

for i in range(1, 52):
    denominador = (2 * i + 1) ** 2
    soma += sinal * (1 / denominador)
    sinal *= -1

pi = (32 * soma) ** (1/3)

print("Valor aproximado de pi:", pi)