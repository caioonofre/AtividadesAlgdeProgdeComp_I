dinheiro = 1000000000.00

valor_salario = float(input("Insira O valor do salário mínimo: "))

print(f'O valor disponibilizado pelo Governo é de R$ {dinheiro}\n\nCom o salário mínimo sendo R$ {valor_salario}\nComo a base para ser feita uma casa é de 90 salários mínimos.\nEntão poderão ser feitas {dinheiro//(valor_salario*90)} casas inteiras.\nRestando R$ {dinheiro%(valor_salario*90)}.')