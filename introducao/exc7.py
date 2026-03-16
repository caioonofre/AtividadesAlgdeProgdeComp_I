#variaveis
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))
d = int(input("Insira o valor de D: "))
e = int(input("Insira o valor de E: "))
f = int(input("Insira o valor de F: "))

x = round((c*e - b*f) / (a*e - b*d), 1)
y = round((a*f - c*d) / (a*e - b*d), 1)

result = (x, y)

print("\nO resultado é: ", result)