sigla = input("Insira a sigla do seu estado[RJ, MG, SP]: ")

if sigla.upper() == "RJ":
  print("Carioca")
elif sigla.upper() == "MG":
  print("Mineiro")
elif sigla.upper() == "SP":
  print("Paulista")
else:
  print("Outro estado")