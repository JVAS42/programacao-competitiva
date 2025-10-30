try:
    n = int(input())

    for i in range(1, n+1):
        for j in range(1, 4):
            if j == 3:
                print(i ** j)
            else:
                print(i ** j, end=' ')
except:
    print('Aconteceu um erro')