import random

# Dimensões predefinidas
m = 2
n = 3
p = 2

random.seed(42)

A = [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]

B = [[random.randint(0, 9) for _ in range(p)] for _ in range(n)]

C = [[0 for _ in range(p)] for _ in range(m)]

for i in range(m):
	for j in range(p):
		soma = 0
		for k in range(n):
			soma += A[i][k] * B[k][j]
		C[i][j] = soma

print('Matriz A:')
for linha in A:
	print(' '.join(map(str, linha)))

print('\nMatriz B:')
for linha in B:
	print(' '.join(map(str, linha)))

print('\nMatriz C (produto A x B):')
for linha in C:
	print(' '.join(map(str, linha)))

