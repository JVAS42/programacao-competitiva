from math import sqrt

def distance(x, y, x2, y2):
    diference_x = x2 - x
    diference_y = y2 - y
    distance = sqrt((pow(diference_x, 2) + pow(diference_y, 2)))
    return distance

x, y = input().split()
x = float(x)
y = float(y)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

print(f'{distance(x, y, x2, y2):.4f}')
