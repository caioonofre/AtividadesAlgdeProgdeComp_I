A = []
S = 0
contador = 0

for i in range(5):
    valor = float(input(f"Digite o valor da posição {i+1}: "))
    A.append(valor)

for i in range(5):
    if A[i] != 0: 
        S += i / A[i]

        if i < A[i]:
            contador += 1
    else:
        print(f"Divisão por zero na posição {i}, valor ignorado.")

print(f"\nValor de S = {S}")
print(f"Quantidade de termos com numerador menor que o denominador: {contador}")