A = [[0 for j in range(6)] for i in range(10)]

for i in range(10):
    for j in range(6):
        if i < j:
            A[i][j] = i / j
        elif i == j:
            A[i][j] = 0
        else:
            A[i][j] = j / i

for i in range(10):
    for j in range(6):
        print(f"{A[i][j]:.2f}", end=" ")
    print()
