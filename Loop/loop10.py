n = int(input("Insira um número para calcular seu fatorial: "))

for f in range(n-1, 0, -1):
  print(f'{n} x {f} = {n}')
  n = n * f
  f -= 1

print(f'Resultado Final {n}')
