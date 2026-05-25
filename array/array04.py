notas = []
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)
notas_abaixo_media = sum(1 for nota in notas if nota < media)

print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas abaixo da média: {notas_abaixo_media}")
