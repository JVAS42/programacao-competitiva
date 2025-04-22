pi = 3.14159

def sphere(r):
    global pi
    volume = (4/3) * pi * pow(r, 3)
    return volume

radius = int(input())
print(f'VOLUME = {sphere(radius):.3f}')
