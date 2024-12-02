def calcular_area (raio):
    n = 3.14159
    return n * pow(raio, 2)

raio = float(input())
print(f'A={calcular_area(raio):.4f}')
