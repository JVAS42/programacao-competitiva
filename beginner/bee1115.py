coordinate = list()
coordinates = list()

while True:
    coordinate = input().split()
    coordinate = list(map(int, coordinate))

    if 0 in coordinate:
        break

    coordinates.append(coordinate[:])
    coordinate.clear()

for i in range(0, len(coordinates)):
    if coordinates[i][0] > 0 and coordinates[i][1] > 0:
        print('primeiro')
    elif coordinates[i][0] < 0 and coordinates[i][1] > 0:
        print('segundo')
    elif coordinates[i][0] < 0 and coordinates[i][1] < 0:
        print('terceiro')
    else:
        print('quarto')