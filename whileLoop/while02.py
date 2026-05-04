par = []
impar = []
cont = 0
while cont < 5:
  n = int(input(f'Insira {cont+1}° número : '))
  if n%2 == 0:
    par.append(n)
  else:
    impar.append(n)
  cont+=1 

for p in range(len(par)):
  print(f'{par[p]} é par')
for i in range(len(impar)):
  print(f'{impar[i]} é impar')