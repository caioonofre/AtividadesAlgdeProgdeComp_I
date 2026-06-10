frase = input("Digite uma frase: ")
frase_limpa = frase.replace(" ", "").lower()
frase_invertida = frase_limpa[::-1]

print(f"A frase digitada é: {frase}")
print(f"A frase limpa é: {frase_limpa}")
print(f"A frase invertida é: {frase_invertida}")

if frase_limpa == frase_invertida:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
