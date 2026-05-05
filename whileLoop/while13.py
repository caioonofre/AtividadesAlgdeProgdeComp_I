from fractions import Fraction

n = int(input("Digite o valor de N: "))

i = 1
den = n
s = 0

while i <= n:
    s = s + (i / den)
    i = i + 1
    den = den - 1

print(f'Valor de S = {s} [decimal]')
print(f'Valor de S = {Fraction(s)} [fração]')


