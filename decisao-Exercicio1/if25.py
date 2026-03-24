print("Equação quadrática\n")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
  print("A equação não possui raízes reais")
elif delta == 0:
  print("A equação possui apenas uma raiz real")
else:
  print("A equação possui duas raízes reais")