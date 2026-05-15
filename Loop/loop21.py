print("Turminha!")
alunos18 = []
alunos20 = []

for i in range(1, 6):
    nome = input(f"\nInsira o nome do {i}° aluno: ")
    idade = int(input(f"Insira a idade do {i}° aluno: "))
    if idade == 18:
        alunos18.append({nome: idade})
    elif idade >= 20:
        alunos20.append({nome: idade})

if alunos18:
    print(f"\nA quantidade de alunos que tem 18 anos é: {len(alunos18)} \nSão eles: \n")
    for aluno in alunos18:
        for nome, idade in aluno.items():
            print(f"{nome} | {idade} anos")

if alunos20:
    print(
        f"\nA quantidade de alunos que tem mais de 20 anos é: {len(alunos20)} \nSão eles\n"
    )
    for aluno in alunos20:
        for nome, idade in aluno.items():
            print(f"{nome} | {idade} anos")
