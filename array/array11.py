vetor1 = []
vetor2 = []

for i in range(10):
    num = float(input(f"Digite o {i + 1}º número: "))
    vetor1.append(num)

    if num % 2 == 0:
        vetor2.append(num * 3)
    else:
        vetor2.append(num / 2)
print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
