from fractions import Fraction

s = 0
cima = 100
baixo = 0
numBaixo = 0

for i in range(21):
    divisao = cima/baixo
    s += divisao
    print("=============")
    print(cima)
    print("--")
    print(baixo)
    cima -= 1
    for f in range(i):
      numBaixo += 1
      baixo = numBaixo * f
      print(f'{numBaixo} x {f} = {baixo}')
      f -= 1
      print(f)

print(f'Valor de S = {s} [decimal]')
print(f'Valor de S = {Fraction(s)} [fração]')