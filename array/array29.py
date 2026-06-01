A = []
B = []
C = []

for i in range(7):
    A.append(int(input(f"Digite o elemento {i + 1} da matriz A: ")))
print("")
for i in range(7):
    B.append(int(input(f"Digite o elemento {i + 1} da matriz B: ")))
print("")
for i in range(7):
    C.append([A[i], B[i]])

print("Matriz C:")
for i in range(7):
    print(C[i])
