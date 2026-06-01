X = [
    [12345, 20, 0, 6, 85],  # Aluno 1
    [67890, 22, 1, 6, 90],  # Aluno 2
    [54321, 19, 0, 6, 92],  # Aluno 3
    [98765, 21, 0, 5, 88],  # Aluno 4
    [11223, 20, 0, 6, 80],  # Aluno 5
]

melhor_matricula = None
melhor_nota = -1

for aluno in X:
    matricula, idade, sexo, curso, nota = aluno
    if sexo == 0 and curso == 6:
        if nota > melhor_nota:
            melhor_nota = nota
            melhor_matricula = matricula

if melhor_matricula is not None:
    print(
        f"Aluno com melhor nota: Matrícula {melhor_matricula}, Nota {melhor_nota} sexo {aluno[2]} curso {aluno[3]}"
    )
else:
    print("Nenhum aluno do sexo 0, curso 6 encontrado.")
