print("Calculadora de Horas da fábrica")

tempo_segundos = int(input("Insira o tempo de duração do evento da fábrica EM SEGUNDOS: "))

print(f'\nO tempo em horas: {(tempo_segundos/60)//60}')
print(f'O tempo em minutos: {tempo_segundos//60}')
print(f'O tempo em segundos: {tempo_segundos}')