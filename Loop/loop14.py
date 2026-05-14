soma = 0
sinal = 1

for i in range(1, 104, 2):
    denominador = (i**3)
    soma += sinal * (1 / denominador)
    sinal *= -1

pi = (32 * soma) ** (1/3)

print("Valor aproximado de pi:", pi)