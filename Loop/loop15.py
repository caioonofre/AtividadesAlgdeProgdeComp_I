s = 0
fat = 1

for i in range(20):
    if i > 0:
        fat *= i
        print(f'fat {fat}')
    x = (100-i) / fat
    s += x
    print(f'Fatorial = {fat:.0f} | x = {x:.0f}') 

print(f'Valor de final S = {s}')