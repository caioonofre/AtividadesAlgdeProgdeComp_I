print("Descubra se um número de 4 dígitos possui a característica especial (explicada no enunciado).")
numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:
    primeiros_dois = numero // 100
    ultimos_dois = numero % 100
    soma = primeiros_dois + ultimos_dois
    if soma ** 2 == numero:
        print(f"{numero} possui a característica: {primeiros_dois} + {ultimos_dois} = {soma} -> {soma}^2 = {numero}")
    else:
        print(f"{numero} não possui a característica.")
else:
    print("Número fora do intervalo permitido (1000 a 9999).")