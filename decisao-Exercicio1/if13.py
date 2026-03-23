nomeTime1 = input("Insira o nome do time 1: ")
golsTime1 = int(input("Insira a quantidade de gols do time 1: "))

nomeTime2 = input("Insira o nome do time 2: ")
golsTime2 = int(input("Insira a quantidade de gols do time 2: "))

if golsTime1 > golsTime2:
  print(f'O time: {nomeTime1} foi o vencedor com {golsTime1} gols!')
elif golsTime2 > golsTime1:
  print(f'O time: {nomeTime2} foi o vencedor com {golsTime2} gols!')
else:
  print("Empate")