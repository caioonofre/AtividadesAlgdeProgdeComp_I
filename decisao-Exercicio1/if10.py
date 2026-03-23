nota1 = float(input("Insira a sua primeira nota: "))
nota2 = float(input("Insira a sua segunda nota: "))

if (nota1+nota2)/2 >= 7:
  print(f'Sua média é {round((nota1+nota2)/2, 2)} e voce foi aprovado!')
else:
  rec = float(input("Insira a nota da recuperação: "))
  mediaFinal = round((nota1+nota2+rec)/3, 2)

  if mediaFinal >= 5:
    print(f'Sua média final é {mediaFinal} e você foi aprovado!')
  else:
    print("Você foi reprovado!")