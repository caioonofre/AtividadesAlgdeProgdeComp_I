mes = int(input("Insira um número de 1 a 12 para eu citar o mês desse número: "))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if mes >= 1 and mes <= 12:
  print(meses[mes-1])
else:
  print("Insira um número válido!")
