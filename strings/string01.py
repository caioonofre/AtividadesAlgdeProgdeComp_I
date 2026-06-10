string1 = input("Digite a primeira frase: ")
string2 = input("Digite a segunda frase: ")

print(f"Primeira frase: {string1} - Tamanho: {len(string1)}")
print(f"Segunda frase: {string2} - Tamanho: {len(string2)}")

if len(string1) == len(string2):
    print("As duas frases possuem o mesmo comprimento.")
else:
    print("As duas frases possuem comprimentos diferentes.")

if string1 == string2:
    print("As duas frases são iguais no conteúdo.")
else:
    print("As duas frases são diferentes no conteúdo.")
