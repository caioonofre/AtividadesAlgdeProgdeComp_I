n = int(input("Insira um número para calcular seu fatorial: "))
f = n-1

while f > 0:
  n = n * f
  print(n)
  f -= 1

print(f'Final {n}')
