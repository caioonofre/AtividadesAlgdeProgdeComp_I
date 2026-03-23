letra = input("Insira uma letra: ")

vogais = ["a", "e", "i", "o", "u"]

if letra.lower() in vogais:
  print(f'A letra {letra} é vogal')
else:
  print(f'A letra {letra} não é vogal')