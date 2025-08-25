x = int(input())
cont = 0

while True:
    if x % 2 == 0:
        x += 1
    else:
        print(x)
        x += 1
        cont += 1
        if cont == 6:
            break