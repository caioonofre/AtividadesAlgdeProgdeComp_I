cont = 99
somaPar = 0
somaImpar = 0

while cont != 1:
  if cont%2 == 0:
    somaPar += 1
  else:
    somaImpar += 1
  cont -= 1

print(f'Soma par: {somaPar}')
print(f'Soma par: {somaImpar}')