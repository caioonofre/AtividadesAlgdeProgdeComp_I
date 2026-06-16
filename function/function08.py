def dia_da_semana(num):
    diasDaSemana = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"]
    if num < 1 or num > 7:
        print("Número inválido. Por favor, insira um número entre 1 e 7.")
    else:
        print(diasDaSemana[num - 1])


numero = int(
    input("Digite um número natural (1-7) para obter o dia da semana correspondente: ")
)
dia_da_semana(numero)
