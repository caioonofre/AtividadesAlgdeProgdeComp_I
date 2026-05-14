biscoitos_quebrados = 0
for hora in range(1, 17):
    if hora == 1:
        biscoitos_quebrados = 1
        print(f"Hora {hora}: {biscoitos_quebrados} biscoitos quebrados")
    else:
        biscoitos_quebrados *= 3
        print(f"Hora {hora}: {biscoitos_quebrados} biscoitos quebrados")

print(f"Total de biscoitos quebrados no final do dia: {biscoitos_quebrados}")
