leaderboards = list()

def data():
    scoreboard = input().split()
    scoreboard = list(map(int, scoreboard))

    leaderboards.append(scoreboard[:])
    scoreboard.clear()


def calculate():
    total = 0
    inter = 0
    gremio = 0
    draw = 0

    for i in range(0, len(leaderboards)):
        if leaderboards[i][0] > leaderboards[i][1]:
            inter += 1
        elif leaderboards[i][0] < leaderboards[i][1]:
            gremio += 1
        else:
            draw += 1
        total += 1
    
    print(f'{total} grenais')
    print(f'Inter:{inter}')
    print(f'Gremio:{gremio}')
    print(f'Empates:{draw}')
    if inter > gremio:
        print(f'Inter venceu mais')
    elif inter < gremio:
        print(f'Gremio venceu mais')
    else:
        print('Nao houve vencedor')


def menu():
    data()
    while True:
        print('Novo grenal (1-sim 2-nao)')
        opcion = int(input())

        if opcion == 1:
            data()
        elif opcion == 2:
            calculate()
            break
        else:
            continue


menu()