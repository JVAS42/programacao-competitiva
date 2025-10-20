try:
    x = int(input())
    y = int(input())

    if x > y:
        start = y
        end = x
    else:
        start = x
        end = y

    for i in range(start + 1, end):
        if i%5 == 2 or i%5 == 3:
            print(i)
        else:
            continue
        
except:
    print('ERRO')