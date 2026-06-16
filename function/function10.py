def maior_valor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Os valores são iguais."


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = maior_valor(num1, num2)
print(f"O maior valor entre {num1} e {num2} é: {resultado}")
