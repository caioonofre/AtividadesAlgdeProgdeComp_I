nome = input("Insira seu nome: ")
ano = int(input("Insria seu ano de nascimento: "))

if ano > 1900 and ano < 2026:
    print(f'Olá {nome}, sua idade é {2026 - ano}')
else:
    print(f'O ano {ano} não é válido')