soma = 0
cont = 0
while cont < 5:
    altura = float(input(f"Digite a altura da {cont+1}° pessoa: "))
    soma = soma + altura
    cont+=1
media = soma / 5

print(f'A média das alturas é:, {media}cm')