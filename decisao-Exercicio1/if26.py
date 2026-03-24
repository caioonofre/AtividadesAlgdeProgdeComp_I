print("Verificação de triângulo\n")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

if a < b + c and b < a + c and c < a + b:
  if a == b == c:
    print("O triângulo é equilátero")
  elif a == b or b == c or c == a:
    print("O triângulo é isósceles")
  else:
    print("O triângulo é escaleno")
else:
  print("Os valores lidos não formam um triângulo")