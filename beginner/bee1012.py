pi = 3.14159

def area(a, b, c):
    global pi
    print(f'TRIANGULO: {(a*c)/2:.3f}\n'
          f'CIRCULO: {pi * pow(c,2):.3f}\n'
          f'TRAPEZIO: {((a+b)*c)/2:.3f}\n'
          f'QUADRADO: {pow(b, 2):.3f}\n'
          f'RETANGULO: {(a*b):.3f}')

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
area(a, b, c)
