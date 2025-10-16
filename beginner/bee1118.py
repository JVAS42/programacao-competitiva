def average():
    average = 0
    cont = 0
    while cont < 2:
        note = float(input())
        if note >= 0 and note <= 10:
            average += note
            cont += 1
        else:
            print('nota invalida')
    print(f'media = {average/2:.2f}')

def menu():
    while True:
        print('novo calculo (1-sim 2-nao)')
        opcion = int(input())

        if opcion == 1:
            average()
        elif opcion == 2:
            exit()
        else:
            continue

average()
menu()