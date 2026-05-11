x = 1.0

while x <= 5.0:
    y = (3 + 2*x + 6*(x**2)) / (7 + 9*x + 16*(x**2))
    print(f'x = {round(x, 1)}  -> y = {round(y, 4)}')
    x += 0.1