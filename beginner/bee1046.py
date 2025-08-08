def game_time(time):
    if time[0] == time[1]:
        print('O JOGO DUROU 24 HORA(S)')
    elif time[0] > time[1]:
        cont = 0
        while time[0] != time[1]:
            cont += 1
            time[0] += 1
            if time[0] == 24:
                time[0] = 0
        print(f'O JOGO DUROU {cont} HORA(S)')
    else:
        cont = 0
        for i in range(time[0], time[1]):
            cont += 1
        print(f'O JOGO DUROU {cont} HORA(S)')
            

hours = input().split()
time = list(map(int, hours))

game_time(time)