cont = 99
somaPar = 0
somaImpar = 0

while cont != 1:
  if cont%2 == 0:
    somaPar += cont
  else:
    somaImpar += cont
  cont -= 1

print(f'Soma par: {somaPar}')
print(f'Soma par: {somaImpar}')