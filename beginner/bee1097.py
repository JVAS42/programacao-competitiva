def sequencia_IJ3():
    j = 5
    for i in range(1, 10, 2):
        for j in range(j+2, j-1, -1):
            print(f'I={i} J={j}')
        j += 2

sequencia_IJ3()