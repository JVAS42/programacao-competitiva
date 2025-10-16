placares = list()

def data():
    placar = input().split()
    placar = list(map(int, placar))

    placares.append(placar[:])
    placar.clear()

def menu():
    data()
    while True:
        opcion = int(input('Novo grenal (1-sim 2-nao)'))

        if opcion == 1:
            data()
        elif opcion == 2:
            print('Placares: ', placares)
            break
        else:
            continue

menu()