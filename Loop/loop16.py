soma = 0
fat = 1
variavelExpoente = 0

var = float(input("Insira o valor da variavel: "))

for i in range(0, 30):
    if i == 0:
        soma += var**i
    else:
        fat *= i
        variavelExpoente = var**i
        calc = (variavelExpoente)/fat
        soma += calc
    print(f'Fatorial = {fat} /n Variavel elevada = {variavelExpoente}')

    print(f'Soma final = {soma}')