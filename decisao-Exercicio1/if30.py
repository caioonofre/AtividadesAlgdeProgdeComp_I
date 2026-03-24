print("Controle de temperatura de um forno que derrete alumínio\n")
temperatura = int(input("Insira a temperatura que o alumínio deverá ser trabalhado: "))
if temperatura <= 500:
  print("Temperatura Inválida")
elif temperatura <= 700 and temperatura > 500:
  print("Aquecimento Ligado em 100%")
elif temperatura < 735 and temperatura > 700:
  print("Aquecimento Ligado em 50%")
elif temperatura >= 735 and temperatura < 780:
  print("Aquecimento Desligado")
elif temperatura > 780 and temperatura < 1000:
  print("Superaquecimento")
else:
  print("Temperatura Inválida")
