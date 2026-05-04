cont = 0
numeros = []
numerosNeg = []
total = 0

while cont < 5:
    n = int(input(f'Insira {cont+1}° número : '))
    if n >= 0:
        numeros.append(n)
    else:
        numerosNeg.append(n)
    cont += 1

if numerosNeg:
    print(f'Os numeros negativos são: {numerosNeg}')
else:
    print('Não há numeros negativos')

for i in range(len(numeros)):
    total += numeros[i]


print(f'A média dos números positivos são: {total/len(numeros)}')