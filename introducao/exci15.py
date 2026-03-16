print("Dados de um automóvel!")

modelo = input("\nInsira o modelo do carro: ")
marca = input("\nInsira a marca do carro: ")
ano = int(input("\nInsira o ano do carro: "))
km_initial = int(input("\nInsira o KM inicial: "))
km_final = int(input("\nInsira o KM final: "))
litros_consumido = float(input("\nInsira o valor de litros de gasolina consumidos: "))
preco_litro = float(input("Insira o valor do Litro de gasolina: "))

distancia = km_final-km_initial
print(f'\n------------Informações do carro------------\nModelo: {modelo} | Marca: {marca} | Ano: {ano}\n\n------------Informações da viagem-----------\nDistância percorrida: {distancia}KM\nLitros consumidos: {litros_consumido}L\nPreço do litro da gasolina: {preco_litro}\n\nTotal a pagar: R${round(preco_litro*litros_consumido, 2)}\nO seu carro faz {round(distancia/litros_consumido, 2)}KM/L')