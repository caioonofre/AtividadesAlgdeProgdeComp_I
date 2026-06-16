def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


temp_f = int(input("Digite a temperatura em Fahrenheit: "))
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f} graus Fahrenheit é igual a {temp_c:.2f} graus Celsius")
