qtdTurma = 0
qtdMulher = 0
somaTurma = 0
somaMulher = 0

n = int(input("Qual é a quantidade de pessoas que você pretende inserir?: "))

for i in range(1, n + 1):
    altura = int(input(f"\nInsira a altura da {i}° pessoa [cm]: "))
    sexo = input(f"Insira o sexo da {i}° pessoa[M para masculino e F para feminino]: ")

    while sexo.upper() != "M" and sexo.upper() != "F":
        print("\nINSIRA APENAS M OU F")
        sexo = input(
            f"Insira novamente o sexo da {i}° pessoa[M para masculino e F para feminino]: "
        )

    if sexo.upper() == "F":
        qtdMulher += 1
        somaMulher += altura

    qtdTurma += 1
    somaTurma += altura

print(
    f"\nA quantidade de pessoas na turma é: {qtdTurma} | E a média de altura da turma é: {somaTurma / qtdTurma:.2f}cm"
    f"\nA quantidade de mulheres na turma é: {qtdMulher} | E a média de altura das mulheres é: {somaMulher / qtdMulher:.2f}cm"
)
