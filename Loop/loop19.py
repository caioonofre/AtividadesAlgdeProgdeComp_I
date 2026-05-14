n = int(input("Digite a quantidade de números inteiros: "))

for _ in range(n):
    num = int(input("Digite um número inteiro: "))
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    print(f"Divisores de {num}: {divisores}")
    print(f"Quantidade de divisores: {len(divisores)}")
