import random

A = []
for i in range(20):
    row = [random.randint(1, 10) for _ in range(30)]
    A.append(row)

X = [random.randint(1, 10) for _ in range(30)]

Y = []
for i in range(20):
    sum_product = 0
    for j in range(30):
        sum_product += A[i][j] * X[j]
    Y.append(sum_product)
print("Matriz A:")
for row in A:
    print(row)

print("\nVetor X:")
print(X)

print("Vetor Y resultante:")
print(Y)
