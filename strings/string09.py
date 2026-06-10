def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    return cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito)


cpf_input = input("Digite um número de CPF (xxx.xxx.xxx-xx): ")
if validar_cpf(cpf_input):
    print(f"CPF {cpf_input} é válido.")
else:
    print(f"CPF {cpf_input} é inválido.")
