from fractions import Fraction

dvsor = 1
ddendo = 1
soma = dvsor/ddendo

while ddendo < 100:
  ddendo += 1
  soma = (soma) + (dvsor/ddendo)


print(f'Resultado em decimal {soma}')
print(f'Resultado em fração {Fraction(soma)}')