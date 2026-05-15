print("Controle de Consumo da Viagem")

reabastecimentos = int(input("Digite o número total de reabastecimentos: "))

odometro_anterior = float(input("Digite o valor inicial do odômetro: "))

total_km = 0
total_litros = 0

for i in range(1, reabastecimentos + 1):
    print(f"\nParada {i}")

    odometro_atual = float(input("Digite o valor do odômetro: "))
    litros = float(input("Digite a quantidade de combustível abastecida: "))

    km_rodados = odometro_atual - odometro_anterior
    consumo = km_rodados / litros

    print(f"Quilometragem por litro nesta parada: {consumo:.2f} km/l")

    total_km += km_rodados
    total_litros += litros

    odometro_anterior = odometro_atual

media = total_km / total_litros

print(f"\nQuilometragem média da viagem: {media:.2f} km/l")