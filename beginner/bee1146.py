while True:
    x = int(input())
    i = 1

    if x == 0:
        break
    else:
        while i < x:
            print(i, end=' ')
            i += 1
        print(i)
        i = 1