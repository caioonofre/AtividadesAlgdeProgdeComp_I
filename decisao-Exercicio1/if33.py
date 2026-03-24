print("Digite as idades de 2 homens:")
homem1 = int(input("Idade do primeiro homem: "))
homem2 = int(input("Idade do segundo homem: "))

print("Digite as idades de 2 mulheres:")
mulher1 = int(input("Idade da primeira mulher: "))
mulher2 = int(input("Idade da segunda mulher: "))


if homem1 == homem2 or mulher1 == mulher2:
    print("As idades devem ser diferentes para cada grupo.")
else:
    if homem1 > homem2:
        homem_mais_velho = homem1
        homem_mais_novo = homem2
    else:
        homem_mais_velho = homem2
        homem_mais_novo = homem1

    if mulher1 > mulher2:
        mulher_mais_velha = mulher1
        mulher_mais_nova = mulher2
    else:
        mulher_mais_velha = mulher2
        mulher_mais_nova = mulher1

    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    print(f"Soma das idades do homem mais velho com a mulher mais nova: {soma}")
    print(f"Produto das idades do homem mais novo com a mulher mais velha: {produto}")