vetor1 = []
vetor2 = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número do vetor 1: "))
    vetor1.append(num)
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número do vetor 2: "))
    vetor2.append(num)
vetor3 = []
for i in range(10):
    soma = vetor1[i] + vetor2[i]
    vetor3.append(soma)

print("VETOR 1:", end=" ")
for num in vetor1:
    print(f"{num:.2f}", end=" ")
print("\nVETOR 2:", end=" ")
for num in vetor2:
    print(f"{num:.2f}", end=" ")
print("\nVETOR 3:", end=" ")
for num in vetor3:
    print(f"{num:.2f}", end=" ")
