'''

A = sides[0]
B = sides[1]
C = sides[2]

'''
def triangle_types(sides):
    sides.sort(reverse=True)
    if sides[0] >= sides[1] + sides[2]:
        print('NAO FORMA TRIANGULO')
    else:
        if pow(sides[0], 2) == pow(sides[1], 2) + pow(sides[2], 2):
            print('TRIANGULO RETANGULO')
        if pow(sides[0], 2) > pow(sides[1], 2) + pow(sides[2], 2):
            print('TRIANGULO OBTUSANGULO')
        if pow(sides[0], 2) < pow(sides[1], 2) + pow(sides[2], 2):
            print('TRIANGULO ACUTANGULO')
        if sides[0] == sides[1] == sides[2]:
            print('TRIANGULO EQUILATERO')
        if sides[0] == sides[1] != sides[2] or sides[0] == sides[2] != sides[1] or sides[1] == sides[2] != sides[0]:
            print('TRIANGULO ISOSCELES')

values = input().split()
sides = list(map(float, values))

triangle_types(sides)