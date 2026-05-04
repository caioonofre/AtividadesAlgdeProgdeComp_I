n = int(input("Quantos atletas deseja cadastrar? "))

contador = 0
soma = 0

while contador < n:
    inscricao = int(input("Digite o número de inscrição: "))
    altura = float(input("Digite a altura em cm: "))

    soma = soma + altura

    if contador == 0:
        maior_altura = altura
        menor_altura = altura
        insc_maior = inscricao
        insc_menor = inscricao
    else:
        if altura > maior_altura:
            maior_altura = altura
            insc_maior = inscricao

        if altura < menor_altura:
            menor_altura = altura
            insc_menor = inscricao

    contador = contador + 1

media = soma / n

print("Atleta mais alto:")
print(f'Inscrição: {insc_maior}')
print(f'Altura: {maior_altura}')
print("")

print("Atleta mais baixo:")
print(f'Inscrição: {insc_menor}')
print(f'Altura: {menor_altura}')
print("")

print(f'Altura média do grupo: {media}')