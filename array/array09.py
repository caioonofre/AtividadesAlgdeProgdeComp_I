array1 = []
array2 = []
print("Digite os elementos do primeiro array:")
for i in range(5):
    num = int(input(f"Elemento {i + 1}: "))
    array1.append(num)

print("Digite os elementos do segundo array:")
for i in range(5):
    num = int(input(f"Elemento {i + 1}: "))
    array2.append(num)

intercalado = []
for i in range(5):
    intercalado.append(array1[i])
    intercalado.append(array2[i])

print("Array intercalado:")
print(intercalado)
