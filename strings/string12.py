telefone = input("Telefone: ")
telefone = telefone.replace("-", "")
if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    telefone = "3" + telefone
    print("Telefone corrigido sem formatação:", telefone)
    print("Telefone corrigido com formatação:", telefone[:4] + "-" + telefone[4:])
else:
    print("Telefone possui", len(telefone), "dígitos. Não é necessário corrigir.")
