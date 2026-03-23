n1 = int(input("Insira o primeiro número para soma: "))
n2 = int(input("Insira o segundo númeor par soma: "))

soma = n1+n2

if soma > 10:
    print(f'A soma: {n1} + {n2} = {soma} é maior que 10!')
elif soma < 10:
    print(f'A soma: {n1} + {n2} = {soma} é menor que 10!')
else:
    print(f'A soma: {n1} + {n2} = {soma} é  igual a 10!')