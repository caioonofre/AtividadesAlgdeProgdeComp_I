from fractions import Fraction

ddendo = 1
soma = 0

for i in range(100):
  dvisao = 1/ddendo
  soma += dvisao
  ddendo += 1


print(f'Resultado em decimal {soma}')
print(f'Resultado em fração {Fraction(soma)}')