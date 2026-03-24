print("Calculadora de média e conceito\n")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
  print(f'A média é {media} e o conceito é A')
  print("APROVADO")
elif media >= 7.5 and media < 9:
  print(f'A média é {media} e o conceito é B')
  print("APROVADO")
elif media >= 6 and media < 7.5:
  print(f'A média é {media} e o conceito é C')
  print("APROVADO")
elif media >= 4 and media < 6:
  print(f'A média é {media} e o conceito é D')
  print("REPROVADO")
else:
  print(f'A média é {media} e o conceito é E')
  print("REPROVADO")