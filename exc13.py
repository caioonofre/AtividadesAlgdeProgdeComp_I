# Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto
# vai gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que
# leia:
# • A distância da casa de Maria até sua irmã;
# • O consumo do carro de Maria (KM rodados / litro);
# • O preço da gasolina (litro).
# E mostre as informações que Maria necessita.

print("Calculador de gosolina!\n")

distancia = float(input("Insira a distância que você deseja chegar[EM KILOMETROS KM]: "))
consumo = float(input("\nInsira o consumo que seu carro faz[KM POR LITRO KM/L]: "))
preco = float(input("\nInsira o valor da Gasolina[R$]: "))

gastado = round((distancia/consumo)*preco, 2)
gasolina = round(distancia/consumo, 2)
print(f'\nVocê terá que colocar {gasolina} Litros.\nO valor que você gastará para chegar no local é: R${gastado}')
