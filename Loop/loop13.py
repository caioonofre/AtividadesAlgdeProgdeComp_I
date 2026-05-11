from fractions import Fraction

n = int(input("Digite o valor de N: "))

s = 0
cima = 1
baixo = n

for i in range(n, 0, -1):
    divisao = cima/baixo
    s += divisao
    print("=============")
    print(cima)
    print("--")
    print(baixo)
    cima += 1
    baixo -= 1

print(f'Valor de S = {s} [decimal]')
print(f'Valor de S = {Fraction(s)} [fração]')


