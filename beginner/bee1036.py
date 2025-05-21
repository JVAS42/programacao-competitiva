import math

def bhaskara(a, b, c):
    if a == 0:
        print('Impossível calcular')
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

bhaskara(a, b, c)
