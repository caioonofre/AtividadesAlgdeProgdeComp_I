n1 = int(input("Insira o número para saber se é positivo/negativo ou 0: "))

if n1 > 0:
    print(f'{n1} é positivo!')
elif n1 < 0:
    print(f'{n1} é negativo!')
else:
    print(f'O número é: {n1}')