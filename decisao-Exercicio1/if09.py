nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 6:
  print(f'Sua média é: {media}, você foi aprovado!')
else:
  print(f'Sua média é {media}, você foi reprovado!')