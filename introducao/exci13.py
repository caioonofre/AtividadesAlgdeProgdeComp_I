print("Calculador de gosolina!\n")

distancia = float(input("Insira a distância que você deseja chegar[EM KILOMETROS KM]: "))
consumo = float(input("\nInsira o consumo que seu carro faz[KM POR LITRO KM/L]: "))
preco = float(input("\nInsira o valor da Gasolina[R$]: "))

gastado = round((distancia/consumo)*preco, 2)
gasolina = round(distancia/consumo, 2)
print(f'\nVocê terá que colocar {gasolina} Litros.\nO valor que você gastará para chegar no local é: R${gastado}')
