A = []
S = 0

for i in range(20):
    valor = float(input(f"Digite o valor da posição {i+1}: "))
    A.append(valor)

for i in range(10):
    S += (A[i] - A[19 - i]) ** 2

print(f"\nValor de S = {S}")
