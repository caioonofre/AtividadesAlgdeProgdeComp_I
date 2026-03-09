print("A calculadora do seu salário!")

salario_bruto = float(input("Insira seu salário bruto: "))
salario_liuqido = salario_bruto - ((salario_bruto*0.15) + (salario_bruto*0.11) + (salario_bruto*0.03))

print(f'\nO IR(Imposto de renda) descontado do seu salário é: R${salario_bruto*0.15}\nO INSS descontado do seu salário é de: R${salario_bruto*0.11}\nO valor descontado pelo Síndicato do seu salário é: R${salario_bruto*0.03}\n\nO valor que Sobrou(salário líquido) é de: R${salario_liuqido}')