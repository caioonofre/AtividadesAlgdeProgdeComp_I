print("Média Ponderada de um aluno!")
print("\nMédia para aprovação = nota 6")

nome = input("\nInsira seu nome: ")
nota1 = float(input("\nInsira a primeira nota (Peso 2): "))
nota2 = float(input("\nInsira a segunda nota (Peso 3): "))
nota3 = float(input("\nInsira a terceira nota (Peso 5): "))

resposta = ((nota1*2) + (nota2*3) + (nota3*5)) / 10

print(f'\nOlá {nome} sua média é {resposta}')

if resposta >= 6:
  print(f'Parabéns {nome}! Você foi aprovado!!!')
else:
  print(f'Olá {nome}, você foi reprovado.')