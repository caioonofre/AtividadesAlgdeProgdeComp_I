horasProfessor1 = float(input("Insira a quantidade de horas dadas pelo primeiro professor: "))
valorProfessor1 = float(input("Insira o valor da hora do primeiro professor: "))

horasProfessor2 = float(input("\nInsira a quantidade de horas dadas pelo segundo professor: "))
valorProfessor2 = float(input("Insira o valor da hora do segundo professor: "))

prof1 = horasProfessor1*valorProfessor1
prof2 = horasProfessor2*valorProfessor2

if prof1 > prof2:
  print("O professor 1 tem o salário maior")
else:
  print("O professor 2 tem o salário maior")
