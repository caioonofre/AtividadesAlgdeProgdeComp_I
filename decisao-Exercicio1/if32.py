print("Algoritmo de operações com duas variáveis inteiras\n")

a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))

resto = a % b

if resto == 1:
    resultado = a + b + resto
    print(f"Soma das variáveis mais o resto: {resultado}")
elif resto == 2:
    if a % 2 == 0:
        print("Primeiro valor é par.")
    else:
        print("Primeiro valor é ímpar.")
    if b % 2 == 0:
        print("Segundo valor é par.")
    else:
        print("Segundo valor é ímpar.")
elif resto == 3:
    soma = a + b
    resultado = soma * a
    print(f"(Soma dos valores) x (primeiro valor) = {resultado}")
elif resto == 4:
    soma = a + b
    if b != 0:
        resultado = soma / b
        print(f"(Soma dos valores) dividido pelo segundo valor = {resultado}")
    else:
        print("Divisão por zero não é permitida.")
else:
    print(f"Quadrado do primeiro valor: {a**2}")
    print(f"Quadrado do segundo valor: {b**2}")
    