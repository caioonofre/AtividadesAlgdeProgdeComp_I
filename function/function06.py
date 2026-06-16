def soma_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma


n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
resultado = soma_intervalo(n1, n2)
print(f"A soma dos números inteiros no intervalo [{n1}, {n2}] é: {resultado}")
